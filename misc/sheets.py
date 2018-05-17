from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class Sheet():
    def __init__(self):
        self.SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        self.store = file.Storage('credentials.json')
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            self.flow = client.flow_from_clientsecrets('client_secret.json', self.SCOPES)
            self.creds = tools.run_flow(self.flow, self.store)
        self.service = build('sheets', 'v4', http=self.creds.authorize(Http()))
    
    def get_data(self):
        SPREADSHEET_ID = '1L8lY0i3DAB9xeMn7BaoFa7cplx-X4l8OAVxVC2tsNeQ'
        RANGE_NAME = 'Assignments!A2:C'
        result = self.service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            return None 
        else:
            return values 
sheet = Sheet()
sheet.get_data()