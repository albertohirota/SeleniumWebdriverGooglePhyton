from enum import Enum




class Sites(Enum):
    GMAIL = 1
    CALENDAR = 2
    DRIVE = 3
    DOCS = 4
    SHEETS = 5
    SLIDES = 6

class GoogleLogin():
    GmailUrl = "https://gmail.com"
    CalendarUrl = "https://calendar.google.com/calendar/"
    DocUrl = "https://docs.google.com/document/u/0/?tgif=d"
    SheetUrl = "https://docs.google.com/spreadsheets/u/0/?tgif=d"
    SlideUrl = "https://docs.google.com/presentation/u/0/?tgif=d"
    DriveUrl = "https://drive.google.com/drive/my-drive?ths=true"
    userName = "eiti.hirota@gmail.com"
    password = "Selenium1"
    Instance = None

    def __init__(self):
        pass

    def GoToGoogleSite(self, site, driverInstance):
        match site:
            case Sites.GMAIL:
                self.LoginToSite(self.GmailUrl, driverInstance)
            case Sites.CALENDAR:
                self.LoginToSite(self.CalendarUrl, driverInstance)
            case Sites.DRIVE:
                self.LoginToSite(self.DriveUrl, driverInstance)
            case Sites.DOCS:
                self.LoginToSite(self.DocUrl, driverInstance)
            case Sites.SHEETS:
                self.LoginToSite(self.SheetUrl, driverInstance)
            case Sites.SLIDES:
                self.LoginToSite(self.SlideUrl, driverInstance)
            case __:
                print("Error in the Website")
    
    def UserLog():
        print("User Login")

    def UserPas():
        print("user Password")

    def LoginToSite(self, url, instance):
        instance.get(url)
        
        UserLog()
        UserPas()