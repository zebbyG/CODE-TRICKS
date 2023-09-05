import json
import os

from google.oauth2.credentials import Credentials # Gets the credentials from the cloud API
from google_auth_oauthlib.flow import InstalledAppFlow # Creates/simplifies the flow of fetching credentials
from googleapiclient.discovery import build # Builds a service object to be sent to the API for authorization
from googleapiclient.errors import HttpError # Logs the HTTP errors.


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly'] # Permission given to the google sheet.


TEST_SURVEY_SPREADSHEET_ID = '1dBGAzEhxxS7inXP__6EpD7KDq6TxI2jHHfgmHEMDs68' # A unique ID to identify the sheet....[change it to your preferable sheet]
TEST_SURVEY_RANGE = '1:1011' # The range of values accessed in the sheet. [match the range of the sheet id specified above]


def main():
    creds = None
    # The script checks if there are any credentials stored in the file <saved_creds.json>
    if os.path.exists('saved_creds.json'):
        creds = Credentials.from_authorized_user_file('saved_creds.json', SCOPES) # Checks if there are any creds in <saved_creds.json>
    if not creds or not creds.valid:
        # When no credentials are found in the file/not valid, it initiates the flow using the InstalledAppFlow, gets the credentials from the file <test_creds.json>
        flow = InstalledAppFlow.from_client_secrets_file(
            'test_creds.json', SCOPES)
        # Prompts for login
        creds = flow.run_local_server(port=0)
        # After login, it saves the credentials in <saved_creds.json>, if you rerun it won't prompt for log in
        with open('saved_creds.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # After getting the creds, the build function creates a service object and sends it to the API,
        # <sheets> is what you are trying to access, <v4> is the version and the credentials to view the sheet
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        # After a successful connection to google sheet API, result variable values specifies what sheet is needed, and what range you want to access.
        result = sheet.values().get(spreadsheetId=TEST_SURVEY_SPREADSHEET_ID,
                                    range=TEST_SURVEY_RANGE).execute()
        # <value> then gets all the values in the range specified for the specific sheet.
        values = result.get('values')
        # Change the Python object to a json string and prints it out
        print(json.dumps(values, indent=4))

        # If not values were found in the sheet
        if not values:
            print('No data found.')
            return
    # If the HTTP connection wasn't successful
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
