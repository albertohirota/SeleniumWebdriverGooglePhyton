import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.CommonFunction import CommonFunction as C
from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Pages.LoginPage import GoogleLogin
from GoogleFramework.Pages.LoginPage import Sites
from GoogleFramework.Pages.SlidesPage import SlidesPage as sp
from GoogleFramework.Base.Validation import Validation as val
from GoogleFramework.Pages.GOfficePage import GOfficePage as GO
from robot.api.deco import keyword
import robot.api.logger
import robot.utils.asserts

@keyword("TC501")
def TC501():
    validation = val.DoesFileExistDocsSheetsSlides("TC501", 10)
    return validation

@keyword("TC502")
def TC502():
    GO.Click_DocumentBlank()
    C.Delay(7)
    GO.RenameDocumentName("TC502")
    GO.Click_ButtonGoogle()
    C.Delay(2)
    validation = val.DoesFileExistDocsSheetsSlides("TC502", 10)
    GO.DeleteFile("TC502")
    return validation

@keyword("TC503")
def TC503():
    GO.Click_OpenFile("TC501")
    validation = val.DoesTextContainsInList("Hello World", sp.GetSlidesTexts(False))
    GO.Click_ButtonGoogle()
    return validation

@keyword("TC504")
def TC504():
    GO.Click_DocumentBlank()
    C.Delay(4)
    GO.RenameDocumentName("TC504")
    C.Delay(1)
    sp.SendText_PresentationBody("TC504 - Hello")
    C.Delay(1)
    GO.RenameDocumentName("TC504")
    C.Delay(1)
    validation = val.DoesTextContainsInList("TC504 - Hello", sp.GetSlidesTexts(True))
    GO.Click_ButtonGoogle()
    GO.DeleteFile("TC504")
    return validation

@keyword("SetupSlides")
def SetupSlides(browser):
    browserDriver = Driver.get_Browser(browser)
    Driver().Initialize(browserDriver)
    GoogleLogin.GoAndLogGoogleSite(Sites.SLIDES)
    C.Delay(5)

@keyword("SlidesCleanUp")
def SlidesCleanUp():
    C.LogInfo("--------Slides Cleanup--------")
    GO.Click_ButtonGoogle()
    files = [ "TC502", "TC504"]
    for file in files:
        while val.DoesFileExistDocsSheetsSlides(file, 3):
            GO.DeleteFile(file)
            C.Delay(2)
    C.Delay(3)
    Driver.CloseBrowser()



#browserDriver = Driver.get_Browser("firefox")
#Driver().Initialize(browserDriver)
#GoogleLogin.GoAndLogGoogleSite(Sites.SLIDES)
#isTrue = TC504()
#print(isTrue)
