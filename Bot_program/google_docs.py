import json
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime

# Authentication for Google Sheets API
def get_google_sheets_service():
    credentials = Credentials.from_service_account_file(
        './credentials.json',
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    # Build the service
    service = build('sheets', 'v4', credentials=credentials)
    return service


# Update Google Sheets with FSM data
async def update_google_sheets(fsm_data):
    SPREADSHEET_ID = '1mXdS_IgVdF1vERnxkdltRWNSBJFRWsMn6Y3aymwBG14'
    TOTAL_USERS_CELL = 'Sheet1!I2'

    # Get the Sheets service
    service = get_google_sheets_service()

    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=TOTAL_USERS_CELL
    ).execute()

    total_users = result.get('values', [])

    RANGE_NAME = ''

    if not total_users:
        total_users = [['0']]
        RANGE_NAME = 'Sheet1!A2:G2'
    else:
        row = int(total_users[0][0]) + 2
        RANGE_NAME = f'Sheet1!A{row}:G{row}'

    # Convert FSM data to a format suitable for Google Sheets
    values1 = [
        [
            fsm_data.get('name'),
            fsm_data.get('consultant'),
            fsm_data.get('doterra_number'),
            fsm_data.get('country'),
            fsm_data.get('city'),
            fsm_data.get('time'),
            datetime.now().strftime("%d.%m.%Y")
        ]
    ]

    body1 = {
        'values': values1
    }

    # Update the values in the sheet
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        body=body1
    ).execute()

    body2 = {
        'values': [[int(total_users[0][0]) + 1]]
    }

    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=TOTAL_USERS_CELL,
        valueInputOption='RAW',
        body=body2
    ).execute()
