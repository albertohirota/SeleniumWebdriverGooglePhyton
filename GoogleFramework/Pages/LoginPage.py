import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction
from enum import Enum
from selenium.webdriver.common.by import By
from Base.Driver import Driver
from Base.Driver import Browser

class Sites(Enum):
    GMAIL = 1
    CALENDAR = 2
    DRIVE = 3
    DOCS = 4
    SHEETS = 5
    SLIDES = 6

class GoogleLogin(CommonFunction):
    GmailUrl = "https://gmail.com"
    CalendarUrl = "https://calendar.google.com/calendar/"
    DocUrl = "https://docs.google.com/document/u/0/?tgif=d"
    SheetUrl = "https://docs.google.com/spreadsheets/u/0/?tgif=d"
    SlideUrl = "https://docs.google.com/presentation/u/0/?tgif=d"
    DriveUrl = "https://drive.google.com/drive/my-drive?ths=true"
    u = "eiti.hirota@gmail.com"
    p = "Selenium1"
    un = "//*[@id='identifierId']"
    nextButton = "//div[@id='identifierNext']"
    pa = "//input[@name='password' or @name='Passwd']"
    logonButton = "//*[@id='passwordNext']"

    def __init__(self):
        pass
    
    def __UserLog():
        CommonFunction.SendKey(By.XPATH, GoogleLogin.un, GoogleLogin.u)
        CommonFunction.Click(By.XPATH, GoogleLogin.nextButton)
        CommonFunction.Delay(4)

    def __UserPas():
        CommonFunction.SendKey(By.XPATH, GoogleLogin.pa, GoogleLogin.p)
        CommonFunction.Click(By.XPATH, GoogleLogin.logonButton)
        CommonFunction.Delay(4)

    def LoginToSite(url):
        CommonFunction.GoToSite(url)
        GoogleLogin.__UserLog()
        GoogleLogin.__UserPas()

    def GoAndLogGoogleSite(site):
        CommonFunction.LogInfo("Loading "+ str(site))
        match site:
            case Sites.GMAIL:
                GoogleLogin.LoginToSite(GoogleLogin.GmailUrl)
            case Sites.CALENDAR:
                GoogleLogin.LoginToSite(GoogleLogin.CalendarUrl)
            case Sites.DRIVE:
                GoogleLogin.LoginToSite(GoogleLogin.DriveUrl)
            case Sites.DOCS:
                GoogleLogin.LoginToSite(GoogleLogin.DocUrl)
            case Sites.SHEETS:
                GoogleLogin.LoginToSite(GoogleLogin.SheetUrl)
            case Sites.SLIDES:
                GoogleLogin.LoginToSite(GoogleLogin.SlideUrl)
            case __:
                CommonFunction.LogError("Website not valid: "+ str(site))
    
    


Driver().Initialize(Browser.CHROME)
GoogleLogin.GoAndLogGoogleSite(Sites.CALENDAR)
