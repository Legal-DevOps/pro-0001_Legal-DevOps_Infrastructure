import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Scopes for Drive and Sheets
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]

class CloudConnector:
    def __init__(self, key_path):
        if not os.path.exists(key_path):
            raise FileNotFoundError(f"Service account key not found at {key_path}")
            
        self.creds = service_account.Credentials.from_service_account_file(
            key_path, scopes=SCOPES
        )
        self.drive_service = build('drive', 'v3', credentials=self.creds)
        self.sheets_service = build('sheets', 'v4', credentials=self.creds)

    def get_or_create_folder(self, folder_name, parent_id=None):
        """Finds or creates a folder on Google Drive."""
        query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
        if parent_id:
            query += f" and '{parent_id}' in parents"
            
        results = self.drive_service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
        files = results.get('files', [])
        
        if files:
            return files[0]['id']
        
        # Create folder if not found
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]
            
        file = self.drive_service.files().create(body=file_metadata, fields='id').execute()
        print(f"[CLOUD] Created folder: {folder_name} (ID: {file.get('id')})")
        return file.get('id')

    def upload_file(self, local_path, folder_id):
        """Uploads a file to a specific folder on Google Drive."""
        file_name = os.path.basename(local_path)
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        
        # Determine mime type or use generic
        media = MediaFileUpload(local_path, resumable=True)
        
        file = self.drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()
        
        # Make file accessible to anyone with the link (optional, for convenience)
        self.drive_service.permissions().create(
            fileId=file.get('id'),
            body={'type': 'anyone', 'role': 'viewer'}
        ).execute()
        
        return file.get('id'), file.get('webViewLink')

    def log_to_sheet(self, spreadsheet_id, values):
        """Appends a row of data to a Google Sheet."""
        body = {
            'values': [values]
        }
        result = self.sheets_service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range='Sheet1!A1',
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        return result

    def create_master_registry(self, folder_id):
        """Creates the Master Registry spreadsheet if it doesn't exist."""
        # Check if already exists in folder
        query = f"name = 'NEXUS_Master_Registry' and mimeType = 'application/vnd.google-apps.spreadsheet' and '{folder_id}' in parents and trashed = false"
        results = self.drive_service.files().list(q=query, spaces='drive', fields='files(id)').execute()
        files = results.get('files', [])
        
        if files:
            return files[0]['id']
            
        spreadsheet = {
            'properties': {
                'title': 'NEXUS_Master_Registry'
            }
        }
        ss = self.sheets_service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
        ss_id = ss.get('spreadsheetId')
        
        # Move to the correct folder
        file = self.drive_service.files().get(fileId=ss_id, fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))
        self.drive_service.files().update(
            fileId=ss_id,
            addParents=folder_id,
            removeParents=previous_parents,
            fields='id, parents'
        ).execute()
        
        # Setup Headers
        headers = ["Timestamp", "Lawyer Email", "Case ID", "Doc Type", "Drive Link", "Status"]
        self.log_to_sheet(ss_id, headers)
        
        print(f"[CLOUD] Created Master Registry (ID: {ss_id})")
        return ss_id

# Usage Example (can be triggered by orchestrator)
if __name__ == "__main__":
    # Test path from .env
    KEY = r"E:\Downloads\--ANTIGRAVITY store\--password\secrets\gcloud-sa.json"
    conn = CloudConnector(KEY)
    
    root_id = conn.get_or_create_folder("NEXUS_LEGAL_DEVOPS_CLOUD")
    registry_id = conn.create_master_registry(root_id)
    print(f"Cloud initialization complete. Registry ID: {registry_id}")
