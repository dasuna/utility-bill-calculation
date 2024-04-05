import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from main_calculation import calculate_ceb_bill
from solar_calculation import calculate_solar_bill
from config import RAW_DATA_FOLDER_ID, OUTPUTS_FOLDER_ID
import datetime

scope = ['https://www.googleapis.com/auth/drive']
service_account_json_key = 'key.json'
credentials = service_account.Credentials.from_service_account_file(
                              filename=service_account_json_key, 
                              scopes=scope)
service = build('drive', 'v3', credentials=credentials)


def get_spreadsheet_id_by_name(folder_id, spreadsheet_name):

    # Call the Drive v3 API to retrieve files in the specified folder
    results = service.files().list(pageSize=1000, fields="nextPageToken, files(id, name, mimeType, size, modifiedTime)",
                                   q=f"'{folder_id}' in parents and trashed=false").execute()

    # Get the files in the folder
    items = results.get('files', [])

    # Search for the spreadsheet by name
    for item in items:
        if item['name'] == spreadsheet_name and item['mimeType'] == 'application/vnd.google-apps.spreadsheet':
            return item['id']  # Return the ID if the name matches

    # Return None if the spreadsheet is not found
    return None