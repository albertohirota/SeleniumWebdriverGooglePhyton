import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.CommonFunction import CommonFunction as C
from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Pages.LoginPage import GoogleLogin
from GoogleFramework.Pages.LoginPage import Sites
from GoogleFramework.Pages.CalendarPage import CalendarPage as cal
from GoogleFramework.Base.Validation import Validation as val
from selenium.webdriver.common.by import By
from robot.api.deco import keyword
import robot.api.logger
import robot.utils.asserts

@keyword("TC201")
def TC201():
    cal.CreateNewEvent()
    cal.Add_Title_SummaryPage("TC201")
    cal.Click_ButtonSaveSummaryPage()
    C.Delay(3)
    validation = val.DoesCalendarEventExist("TC201",3)
    cal.DeleteEvent("TC201")
    return validation

@keyword("TC202")
def TC202():
    cal.CreateNewEvent()
    cal.Add_Title_SummaryPage("TC202")
    cal.Click_ButtonMoreOptionsSummaryPage()
    cal.Add_TextCalendarBody("This is TC202")
    cal.Click_ButtonSave()
    C.Delay(3)
    cal.Click_ExistingEvent("TC202")
    validation = val.DoesCalendarTextMessageBodyExist("This is TC202")
    cal.Click_ButtonDeleteSummaryPage()
    return validation

@keyword("TC203")
def TC203():
    cal.CreateNewEvent()
    cal.Add_Title_SummaryPage("TC203")
    cal.Click_ButtonMoreOptionsSummaryPage()
    C.WaitElementBePresent(By.XPATH, cal.AddGuest)
    cal.Add_Guest("alberto.hirota@gmail.com")
    cal.Add_TextCalendarBody("This is TC203")
    C.Delay(2)
    cal.Click_ButtonSave()
    cal.Click_ButtonSend()
    C.Delay(1)
    cal.Click_ExistingEvent("TC203")
    validation = val.DoesGuestExist("alberto.hirota@gmail.com")
    cal.Click_ButtonDeleteSummaryPage()
    return validation
    
@keyword("SetupCalendar")
def SetupCalendar(browser):
    browserDriver = Driver.get_Browser(browser)
    Driver().Initialize(browserDriver)
    GoogleLogin.GoAndLogGoogleSite(Sites.CALENDAR)
    C.Delay(5)

@keyword("CalendarCleanUp")
def CalendarCleanUp():
    C.LogInfo("--------Calendar Cleanup--------")
    events = [ "TC201" ,"TC202", "TC203"]
    for ev in events:
        while val.DoesCalendarEventExist(ev, 3):
            cal.DeleteEvent(ev)
            cal.Click_ButtonSend()
            C.Delay(2)
    C.Delay(3)
    Driver.CloseBrowser()



#browserDriver = Driver.get_Browser("chrome")
#Driver().Initialize(browserDriver)
#GoogleLogin.GoAndLogGoogleSite(Sites.CALENDAR)
#isTrue = Calendar("chrome").TC201()
