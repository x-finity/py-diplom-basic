import requests

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload,MediaIoBaseDownload
import io

# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))

def test_function():
    print('gdrive test function')

client = pydrive.auth.GoogleAuth()
client.authenticate()

class GoogleDriveAPIClient:
   base_url = 'https://www.googleapis.com/drive/v3'
