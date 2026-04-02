import sys
from pathlib import Path
sys.path.append(r"E:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\LEGAL_DEVOPS\scripts")
from nexus_mail_listener_v1 import authenticate_gmail, send_reply, json

OUTBOX_DIR = Path(r"E:\Downloads\--ANTIGRAVITY store\pro-0001_Legal-DevOps_Infrastructure\PROJECT\NEXUS_CORE\outbox")

service = authenticate_gmail()
for rf in OUTBOX_DIR.glob("response_*.json"):
    print(f"Found: {rf}")
    with open(rf, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Sending to {data['sender']}...")
    send_reply(service, data['sender'], data['subject'], data['response_body'], data.get('attachments', []))
    rf.unlink()
    print("Done.")
