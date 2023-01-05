import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By
from GoogleFramework.Base.GoogleApi import GoogleApi as GApi

class SheetsPage(C):
    sh = "Sheet1"

    def GetSheetsEntry(entry):
        C.LogInfo("Getting Google Sheets spreadshet")
        service = GApi.GetSheetsService()
        SpreadsheetId = GApi.GetCurrentGoogleDocID("sheets")
        sheet = service.spreadsheets()
        fullRange = SheetsPage.sh+"!"+entry
        result = sheet.values().get(spreadsheetId=SpreadsheetId, range=fullRange).execute()
        values = result.get('values',[])

        return values
        
    def SendKeysOnSheet(entryCellRange, text, shares = False):
        C.LogInfo("Sending Keys to Spreadsheet")
        service = GApi.GetSheetsService(shares)
        SpreadsheetId = GApi.GetCurrentGoogleDocID("sheets")
        #range = SheetsPage.sh+"!"+entryCellRange
        values = [[text,text],[text,text]]
        body = {'values':values}
        result = service.spreadsheets().values().update(
            spreadsheetId=SpreadsheetId, range=entryCellRange, valueInputOption="USER_ENTERED", body=body
        ).execute()
        C.LogInfo("Send keys to Sheets, append response: "+str(result))
        