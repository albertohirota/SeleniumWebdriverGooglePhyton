import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.CommonFunction import CommonFunction as C
from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Pages.LoginPage import GoogleLogin
from GoogleFramework.Pages.LoginPage import Sites
from GoogleFramework.Pages.SheetsPage import SheetsPage as sp
from GoogleFramework.Base.Validation import Validation as val
from GoogleFramework.Pages.GOfficePage import GOfficePage as GO
from robot.api.deco import keyword
import robot.api.logger
import robot.utils.asserts

@keyword("TC401")
def TC401():
    validation = val.DoesFileExistDocsSheetsSlides("TC401", 10)
    return validation

@keyword("TC402")
def TC402():
    GO.Click_DocumentBlank()
    C.Delay(7)
    GO.RenameDocumentName("TC402")
    GO.Click_ButtonGoogle()
    C.Delay(2)
    validation = val.DoesFileExistDocsSheetsSlides("TC402", 10)
    GO.DeleteFile("TC402")
    return validation

@keyword("TC403")
def TC403():
    GO.Click_OpenFile("TC401")
    C.Delay(5)
    validation = val.DoesTextContainsInList("Test Case 401", sp.GetSheetsEntry("A2"))
    GO.Click_ButtonGoogle()
    return validation

@keyword("TC404")
def TC404():
    GO.Click_DocumentBlank()
    C.Delay(4)
    GO.RenameDocumentName("TC404")
    C.Delay(1)
    sp.SendKeysOnSheet("A1:B2","TC404 - Hello",True)
    C.Delay(1)
    GO.RenameDocumentName("TC404")
    C.Delay(1)
    validation = val.DoesTextContainsInList("TC404 - Hello", sp.GetSheetsEntry("A1"))
    GO.Click_ButtonGoogle()
    GO.DeleteFile("TC404")
    return validation

@keyword("SetupSheets")
def SetupSheets(browser):
    browserDriver = Driver.get_Browser(browser)
    Driver().Initialize(browserDriver)
    GoogleLogin.GoAndLogGoogleSite(Sites.SHEETS)
    C.Delay(5)

@keyword("SheetsCleanUp")
def SheetsCleanUp():
    C.LogInfo("--------Sheets Cleanup--------")
    GO.Click_ButtonGoogle()
    files = [ "TC402", "TC404"]
    for file in files:
        while val.DoesFileExistDocsSheetsSlides(file, 3):
            GO.DeleteFile(file)
            C.Delay(2)
    C.Delay(3)
    Driver.CloseBrowser()




#browserDriver = Driver.get_Browser("firefox")
#Driver().Initialize(browserDriver)
#GoogleLogin.GoAndLogGoogleSite(Sites.SHEETS)
#isTrue = TC403()
#print(isTrue)
