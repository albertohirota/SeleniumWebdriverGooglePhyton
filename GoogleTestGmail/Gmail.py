import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.CommonFunction import CommonFunction as C
from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Pages.LoginPage import GoogleLogin
from GoogleFramework.Pages.LoginPage import Sites
from GoogleFramework.Pages.GmailPage import GmailPage as gm
from GoogleFramework.Base.Validation import Validation as val
from selenium.webdriver.common.by import By
from robot.api.deco import keyword
import robot.api.logger
import robot.utils.asserts

@keyword("TC001")
def TC001():
    gm.Click_NewEmail()
    C.Delay(3)
    validation = val.IsElementVisible(By.XPATH, gm.ButtonSend)
    gm.Click_ButtonDiscard()
    return validation

@keyword("TC002")
def TC002():
    gm.Click_NewEmail()
    C.Delay(3)
    validation = val.IsTextElementValid(By.XPATH, gm.TitleEmail, "New Message")
    gm.Click_ButtonDiscard()
    return validation

@keyword("TC003")
def TC003():
    gm.Click_NewEmail()
    C.Delay(3)
    gm.Click_ButtonDiscard()
    C.Delay(1)
    validation = val.IsElementNotVisible(By.XPATH, gm.TitleEmail)
    return validation

@keyword("TC004")
def TC004():
    gm.Click_NewEmail()
    C.Delay(3)
    gm.PopulateEmail("albertohirota@gmail.com", "Test Receiving", "Test body receiving email", "alberto.hirota@gmail.com", "eitihirota@gmail.com")
    gm.Click_SendEmail()
    C.Delay(2)
    gm.WaitAndOpenReceivedEmail("Test Receiving")
    validation = val.DoesObjectExist("eitihirota@gmail.com", "email", "span")
    return validation

@keyword("TC005")
def TC005():
    gm.Click_NewEmail()
    C.Delay(3)
    gm.PopulateEmail("albertohirota@gmail.com", "Test Receiving", "Test body receiving email", "alberto.hirota@gmail.com", "eitihirota@gmail.com")
    gm.Click_SendEmail()
    C.Delay(2)
    gm.WaitAndOpenReceivedEmail("Test Receiving")
    validation = val.IsElementVisible(By.XPATH, gm.ButtonReplyAll)
    return validation

@keyword("TC006")
def TC006():
    gm.Click_NewEmail()
    C.Delay(3)
    gm.PopulateEmail("albertohirota@gmail.com", "Test Receiving", "Test body receiving email", "alberto.hirota@gmail.com", "eitihirota@gmail.com")
    gm.Click_SendEmail()
    C.Delay(2)
    gm.WaitAndOpenReceivedEmail("Test Receiving")
    validation = val.DoesObjectExist("albertohirota@gmail.com", "email", "span")
    return validation

@keyword("TC007")
def TC007():
    gm.Click_NewEmail()
    C.Delay(3)
    gm.PopulateEmail("albertohirota@gmail.com", "Test Receiving", "Test body receiving email", "alberto.hirota@gmail.com", "eitihirota@gmail.com")
    gm.Click_SendEmail()
    C.Delay(2)
    gm.WaitAndOpenReceivedEmail("Test Receiving")
    gm.Click_ButtonForward()
    gm.SendKeyAndEnter(By.XPATH, gm.To, "eitihirota@gmail.com")
    gm.Click_SendEmail()
    C.Delay(3)
    gm.GoToInbox()
    gm.GoToInbox()
    validation = val.IsTextElementValid(By.XPATH, gm.InboxListNewEmail, "Forwarded message")
    return validation

@keyword("SetupGmail")
def SetupGmail(browser):
    browserDriver = Driver.get_Browser(browser)
    Driver().Initialize(browserDriver)
    GoogleLogin.GoAndLogGoogleSite(Sites.GMAIL)
    C.Delay(5)

@keyword("GmailCleanUp")
def GmailCleanUp():
    C.LogInfo("--------Gmail Cleanup--------")
    gm.GoToInbox()
    C.Delay(2)
    gm.Click_CheckBoxSelectAll()
    C.Delay(2)
    gm.Click_ButtonDelete()
    C.Delay(2)




browserDriver = Driver.get_Browser("chrome")
Driver().Initialize(browserDriver)
GoogleLogin.GoAndLogGoogleSite(Sites.GMAIL)
IsTrue = TC002()
