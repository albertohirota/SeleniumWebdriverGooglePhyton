import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from enum import Enum
from selenium.webdriver.common.by import By
from Base.Driver import Driver
from Base.Driver import Browser
from decouple import config


class Sites(Enum):
    GMAIL = 1
    CALENDAR = 2
    DRIVE = 3
    DOCS = 4
    SHEETS = 5
    SLIDES = 6

class GoogleLogin(C):
    GmailUrl = "https://gmail.com"
    CalendarUrl = "https://calendar.google.com/calendar/"
    DocUrl = "https://docs.google.com/document/u/0/?tgif=d"
    SheetUrl = "https://docs.google.com/spreadsheets/u/0/?tgif=d"
    SlideUrl = "https://docs.google.com/presentation/u/0/?tgif=d"
    DriveUrl = "https://drive.google.com/drive/my-drive?ths=true"
    u = config("USER")
    p = config("KEY")
    un = "//*[@id='identifierId']"
    nextButton = "//div[@id='identifierNext']"
    pa = "//input[@name='password' or @name='Passwd']"
    logonButton = "//*[@id='passwordNext']"

    def __init__(self):
        pass
    
    def __UserLog():
        C.WaitElementBePresent(By.XPATH, GoogleLogin.un)
        C.SendKey(By.XPATH, GoogleLogin.un, GoogleLogin.u)
        C.Click(By.XPATH, GoogleLogin.nextButton)
        C.Delay(4)

    def __UserPas():
        C.WaitElementBePresent(By.XPATH, GoogleLogin.pa)
        element = C.FindElement(By.XPATH, GoogleLogin.pa)
        element.send_keys(GoogleLogin.p)
        C.Click(By.XPATH, GoogleLogin.logonButton)
        C.Delay(4)

    def LoginToSite(url):
        C.GoToPage(url)
        GoogleLogin.__UserLog()
        GoogleLogin.__UserPas()

    def GoAndLogGoogleSite(site):
        C.LogInfo("Loading "+ str(site))
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
                C.LogError("Website not valid: "+ str(site))
    
    


Driver().Initialize(Browser.CHROME)
GoogleLogin.GoAndLogGoogleSite(Sites.CALENDAR)
