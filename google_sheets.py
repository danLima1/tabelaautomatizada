import os
import json
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials

# Load credentials from the JSON file
credentials = Credentials.from_service_account_file('credentials.json')
scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])

# ID of the spreadsheet (you need to create a new Google Sheet and copy its ID here)
SPREADSHEET_ID = 'your_spreadsheet_id'

def add_entry(sheet_name, data):
    try:
        service = build('sheets', 'v4', credentials=scoped_credentials)
        sheet = service.spreadsheets()
        body = {'values': [list(data.values())]}
        result = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=f'{sheet_name}!A1',
                                       valueInputOption='RAW', insertDataOption='INSERT_ROWS', body=body).execute()
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def get_data(sheet_name):
    try:
        service = build('sheets', 'v4', credentials=scoped_credentials)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=f'{sheet_name}!A1:Z1000').execute()
        values = result.get('values', [])
        return values
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []

