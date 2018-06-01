from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import configparser

class Sheet():
    def __init__(self):
        self.SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        self.store = file.Storage('credentials.json')
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            self.flow = client.flow_from_clientsecrets('client_secret.json', self.SCOPES)
            self.creds = tools.run_flow(self.flow, self.store)
        self.service = build('sheets', 'v4', http=self.creds.authorize(Http()))
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.defaultConfig = self.config['DEFAULT']
        self.sheet_id = self.defaultConfig['spreadsheet_id']
    
    def get_data(self):
        SPREADSHEET_ID = self.sheet_id
        RANGE_NAME = 'Assignments!A2:D'
        result = self.service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            return None 
        else:
            return values 
    
    def get_squads(self):
        SPREADSHEET_ID = self.sheet_id
        RANGE_NAME = 'SquadAssignments!A2:B'
        result = self.service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            return None 
        else:
            return values 

    def get_raid_schedule(self):
        SPREADSHEET_ID = self.sheet_id
        RANGE_NAME =  'Raids!A2:B5'
        result = self.service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            return None
        else:
            return values