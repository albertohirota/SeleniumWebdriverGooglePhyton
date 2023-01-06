import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.CommonFunction import CommonFunction as C
from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Pages.LoginPage import GoogleLogin
from GoogleFramework.Pages.LoginPage import Sites
from GoogleFramework.Pages.DocsPage import DocsPage as dp
from GoogleFramework.Base.Validation import Validation as val
from GoogleFramework.Pages.GOfficePage import GOfficePage as GO
from robot.api.deco import keyword
import robot.api.logger
import robot.utils.asserts

@keyword("TC301")
def TC301():
    validation = val.DoesFileExistDocsSheetsSlides("TC301", 10)
    return validation

@keyword("TC302")
def TC302():
    GO.Click_DocumentBlank()
    C.Delay(7)
    GO.RenameDocumentName("TC302")
    GO.Click_ButtonGoogle()
    C.Delay(2)
    validation = val.DoesFileExistDocsSheetsSlides("TC302", 10)
    GO.DeleteFile("TC302")
    return validation

@keyword("TC303")
def TC303():
    GO.Click_OpenFile("TC301")
    validation = val.DoesTextContainsInList("Test Case 301 and 303", dp.GetDocumentBody(False))
    GO.Click_ButtonGoogle()
    return validation

@keyword("TC304")
def TC304():
    GO.Click_OpenFile("TC301")
    validation = val.DoesTextContainsInList("Hello World", dp.GetDocumentHeader(False))
    GO.Click_ButtonGoogle()
    return validation

@keyword("TC305")
def TC305():
    GO.Click_DocumentBlank()
    C.Delay(4)
    GO.RenameDocumentName("TC305")
    C.Delay(1)
    dp.SendText_DocumentBody("Test Case 305")
    C.Delay(1)
    GO.RenameDocumentName("TC305")
    C.Delay(1)
    validation = val.DoesTextContainsInList("Test Case 305", dp.GetDocumentBody(True))
    GO.Click_ButtonGoogle()
    GO.DeleteFile("TC305")
    return validation

@keyword("SetupDocs")
def SetupDocs(browser):
    browserDriver = Driver.get_Browser(browser)
    Driver().Initialize(browserDriver)
    GoogleLogin.GoAndLogGoogleSite(Sites.DOCS)
    C.Delay(5)

@keyword("DocsCleanUp")
def DocsCleanUp():
    C.LogInfo("--------Docs Cleanup--------")
    GO.Click_ButtonGoogle()
    files = [ "TC302", "TC305"]
    for file in files:
        while val.DoesFileExistDocsSheetsSlides(file, 3):
            GO.DeleteFile(file)
            C.Delay(2)
    C.Delay(3)
    Driver.CloseBrowser()



#browserDriver = Driver.get_Browser("chrome")
#Driver().Initialize(browserDriver)
#GoogleLogin.GoAndLogGoogleSite(Sites.DOCS)
#isTrue = TC305()
#print(isTrue)
