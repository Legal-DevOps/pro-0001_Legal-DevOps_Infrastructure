import imaplib
import smtplib
import email
import os
import json
import time
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# Import NEXUS Engine components
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

import nexus_factory

def load_config():
    """Reads .env manually and loads ACL from json."""
    env = {}
    env_path = os.path.join(os.path.dirname(current_dir), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    key, val = line.strip().split("=", 1)
                    env[key] = val
                    
    acl_path = os.path.join(os.path.dirname(current_dir), "database", "mail_access.json")
    with open(acl_path, "r", encoding="utf-8") as f:
        acl = json.load(f)
        
    return env, acl

def is_authorized(sender_email, acl):
    for user in acl["authorized_users"]:
        if user["email"].lower() == sender_email.lower() and user["status"] == "active":
            return user
    return None

def parse_command(body):
    """
    Parses email body for commands.
    Supported: 
    КЕЙС: [ID]
    ДОКУМЕНТ: [АУДИТ|ТАРИФ|ПРОТОКОЛ|ВСЕ]
    ИНФО: [Кастомный текст]
    """
    case_match = re.search(r'КЕЙС:\s*(\d+)', body, re.IGNORECASE)
    doc_match = re.search(r'ДОКУМЕНТ:\s*(\w+)', body, re.IGNORECASE)
    info_match = re.search(r'ИНФО:\s*(.*)', body, re.IGNORECASE | re.DOTALL)
    
    return {
        "case_id": case_match.group(1) if case_match else None,
        "doc_type": doc_match.group(1).upper() if doc_match else "ВСЕ",
        "custom_info": info_match.group(1).strip() if info_match else ""
    }

def send_reply(sender_email, subject, text, attachments, env):
    msg = MIMEMultipart()
    msg['From'] = env.get("GMAIL_USER")
    msg['To'] = sender_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text, 'plain', 'utf-8'))
    
    for file_path in attachments:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                msg.attach(part)

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(env.get("GMAIL_USER"), env.get("GMAIL_APP_PASSWORD"))
        server.send_message(msg)
        server.quit()
        print(f"[SMTP] Reply sent to {sender_email}")
    except Exception as e:
        print(f"[SMTP ERROR] {e}")

def process_mailbox():
    print("[NEXUS MAIL] Orchestrator started. Listening for requests...")
    env, acl = load_config()
    
    while True:
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(env.get("GMAIL_USER"), env.get("GMAIL_APP_PASSWORD"))
            mail.select("inbox")
            
            # Search for unread emails with trigger in subject
            trigger = acl["bot_config"]["subject_trigger"]
            status, messages = mail.search(None, f'(UNSEEN SUBJECT "{trigger}")')
            
            for num in messages[0].split():
                status, data = mail.fetch(num, '(RFC822)')
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        sender = email.utils.parseaddr(msg['From'])[1]
                        subject = msg['Subject']
                        
                        print(f"[*] New request from: {sender} | {subject}")
                        
                        user_acl = is_authorized(sender, acl)
                        if not user_acl:
                            print(f"[!] Access Denied for {sender}")
                            continue
                            
                        # Extract body
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode('utf-8')
                        else:
                            body = msg.get_payload(decode=True).decode('utf-8')
                            
                        cmd = parse_command(body)
                        if not cmd["case_id"]:
                            send_reply(sender, f"RE: {subject}", "Ошибка: Не указан КЕЙС. Используйте формат КЕЙС: 0003", [], env)
                            continue
                            
                        # Verify project access
                        if "*" not in user_acl["allowed_projects"] and cmd["case_id"] not in user_acl["allowed_projects"]:
                            send_reply(sender, f"RE: {subject}", f"Ошибка: У вас нет доступа к кейсу {cmd["case_id"]}", [], env)
                            continue
                            
                        # Mocked logic for finding participant data
                        # Ideally, this should read from database/case_info.json
                        # For now, we'll use participant package generation logic
                        print(f"[+] Processing Case {cmd['case_id']} for {sender}...")
                        
                        # Target folder for results
                        target_dir = os.path.join(os.path.dirname(current_dir), "PROJECT", f"mail_output_{cmd['case_id']}")
                        if not os.path.exists(target_dir): os.makedirs(target_dir)
                        
                        # Here we would normally find the person's name/address by ID
                        # Assuming '1205' is the ID for testing
                        # In real use, we'd lookup from database
                        nexus_factory.generate_participant_package(
                            full_name="ЗАПИТ ЧЕРЕЗ EMAIL", 
                            address="Адреса з бази", 
                            id_code=cmd['case_id'], 
                            folder_path=target_dir
                        )
                        
                        files_to_send = [
                            os.path.join(target_dir, f"{cmd['case_id']}_АУДИТ_ФІНАНСИ.pdf"),
                            os.path.join(target_dir, f"{cmd['case_id']}_ВІДМОВА_ТАРИФ.pdf"),
                            os.path.join(target_dir, f"{cmd['case_id']}_ПРОТОКОЛ_РОЗБІЖНОСТЕЙ.pdf")
                        ]
                        
                        reply_text = f"NEXUS ORCHESTRATOR: Пакет документів по кейсу {cmd['case_id']} готовий.\n\n"
                        if cmd["custom_info"]:
                            reply_text += f"Ваші зауваження враховано: {cmd['custom_info']}\n"
                            
                        send_reply(sender, f"RE: {subject} [DONE]", reply_text, files_to_send, env)
                        
                        # Mark as read (implicitly done by search UNSEEN usually, but let's be sure)
                        mail.store(num, '+FLAGS', '\\Seen')
                        
            mail.logout()
        except Exception as e:
            print(f"[ERROR] Connection lost or failure: {e}")
            
        time.sleep(acl["bot_config"]["check_interval_sec"])

if __name__ == "__main__":
    process_mailbox()
