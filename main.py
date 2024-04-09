import flask
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from main_calculation import calculate_ceb_bill
from solar_calculation import calculate_solar_bill
from get_spreadsheet_id_by_name import get_spreadsheet_id_by_name
from config import RAW_DATA_FOLDER_ID, OUTPUTS_FOLDER_ID
import datetime

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)

# Set the timeout to  1200 seconds (20 minutes)
app.config['TIMEOUT'] = 1200

scope = ['https://www.googleapis.com/auth/drive']
service_account_json_key = 'key.json'
credentials = service_account.Credentials.from_service_account_file(
                              filename=service_account_json_key, 
                              scopes=scope)
service = build('drive', 'v3', credentials=credentials)

@app.get("/")
def hello():
    folder_id = RAW_DATA_FOLDER_ID
    # Call the Drive v3 API
    results = service.files().list(pageSize=1000, fields="nextPageToken, files(id, name, mimeType, size, modifiedTime)", q=f"'{folder_id}' in parents and trashed=false").execute()
    # get the results
    items = results.get('files', [])

    for item in items:
        print(item["id"])
        print(item["name"])
        sheet_id = item["id"]
        file_name = item["name"]

        relevant_ratecard_sheet_id = get_spreadsheet_id_by_name(OUTPUTS_FOLDER_ID, file_name)

        current_date = datetime.datetime.now()
        current_year = str(current_date.year)

        try:
            calculate_ceb_bill(sheet_id, current_year, relevant_ratecard_sheet_id)
            calculate_solar_bill(sheet_id, current_year, relevant_ratecard_sheet_id)
        except:
            print(f"An error occurred handling files related to year {current_year} in the file {file_name}")

    """Return a friendly HTTP greeting."""
    return "Hello World!\n"


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)