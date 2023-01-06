from __future__ import print_function
import os.path
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
#from oauth2client.service_account import ServiceAccountCredentials
#from oauth2client import client, file, tools
import re
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from GoogleFramework.Base.CommonFunction import CommonFunction as C
from GoogleFramework.Pages.GOfficePage import GOfficePage as GO
from GoogleFramework.Base.Driver import Driver
from google.oauth2 import service_account

class GoogleApi(C):
    ApplicationName = "GoogleAutomation" 
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/spreadsheets.readonly',
        'https://www.googleapis.com/auth/documents.readonly',
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive.activity.readonly',
        'https://www.googleapis.com/auth/presentations',
        'https://www.googleapis.com/auth/presentations.readonly'
    ]

    def GetCurrentGoogleDocID(app):
        regex = ""
        C.LogInfo("Getting Google Document Id for app: "+ app)
        match app.lower():
            case "docs":
                regex = "/document/d/([a-zA-Z0-9-_]+)"
            case "sheets":
                regex = "/spreadsheets/d/([a-zA-Z0-9-_]+)"
            case "slides":
                regex = "/presentation/d/([a-zA-Z0-9-_]+)"
        
        URL =  Driver.get_Instance().current_url
        try:    
            idAll =  re.search(regex,URL).group()
        except:
            C.Delay(5)
            idAll =  re.search(regex,URL).group()
        id = idAll[idAll.find('/d/')+3:]
        C.LogInfo("Id found python is: " + id)
        return id
    
    def GetCredential(runShareFile):
        if runShareFile:
            GO.SharePublic("automation@southern-bonsai-370413.iam.gserviceaccount.com")
        
        json = str(os.getcwd())+"\\GoogleFramework\\Attachments\\Google.json"
        credential = service_account.Credentials.from_service_account_file(json,scopes=GoogleApi.scope)
        return credential

    def GetSheetsService(runShareFile = False):
        C.LogInfo("Getting Google Sheets Service")
        creds = GoogleApi.GetCredential(runShareFile)
        service = build('sheets', 'v4', credentials=creds)
        return service 

    def GetDocsService(runShareFile = False):
        C.LogInfo("Getting Google Docs Service")
        creds = GoogleApi.GetCredential(runShareFile)
        service = build('docs', 'v1', credentials=creds)
        return service 

    def GetSlidesService(runShareFile = False):
        C.LogInfo("Getting Google Slides Service")
        creds = GoogleApi.GetCredential(runShareFile)
        service = build('slides', 'v1', credentials=creds)
        return service   

    def GetDriveService(runShareFile = False):
        C.LogInfo("Getting Google Drive Service")
        creds = GoogleApi.GetCredential(runShareFile)
        service = build('drive', 'v3', credentials=creds)
        return service   
            
