import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.CommonFunction import CommonFunction as C
from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Pages.LoginPage import GoogleLogin
from GoogleFramework.Pages.LoginPage import Sites
from GoogleFramework.Pages.GDrivePage import GDrivePage as gdp
from GoogleFramework.Base.Validation import Validation as val
from GoogleFramework.Pages.GOfficePage import GOfficePage as GO
from robot.api.deco import keyword
import robot.api.logger
import robot.utils.asserts

@keyword("TC101")
def TC101():
    validation = val.DoesFileInGDriveExists("TC101", 10)
    return validation

@keyword("TC102")
def TC102():
    gdp.Click_DriveMenuFolder("Shared with me")
    C.Delay(5)
    validation = val.DoesFileInGDriveExists("logo Lambton.PNG", 10)
    gdp.Click_DriveMenuFolder("My Drive")
    return validation

@keyword("TC103")
def TC103():
    gdp.Click_NewFile()
    gdp.Click_GoogleDocs()
    C.GoToTab(1)
    C.Delay(8)
    GO.RenameDocumentName("TC103")
    C.Delay(5)
    C.CloseTab(1)
    C.GoToTab(0)
    C.Delay(10)
    validation = val.DoesFileInGDriveExists("TC103", 10)
    gdp.DeleteFileInDrive("TC103")
    return validation

@keyword("TC104")
def TC104():
    validation = val.DoesTextContainsInList("TC301",gdp.GetFileList())
    return validation

@keyword("SetupGDrive")
def SetupGDrive(browser):
    browserDriver = Driver.get_Browser(browser)
    Driver().Initialize(browserDriver)
    GoogleLogin.GoAndLogGoogleSite(Sites.DRIVE)
    C.Delay(5)

@keyword("GDriveCleanUp")
def GDriveCleanUp():
    C.LogInfo("--------Google Drive Cleanup--------")
    GO.Click_ButtonGoogle()
    files = [ "Untitled document", "TC103","TC302","TC305","TC402", "Untitled spreadsheet", 
                "TC404", "TC502", "TC504","Untitled presentation"]
    for file in files:
        while val.DoesFileInGDriveExists(file, 0):
            gdp.DeleteFileInDrive(file)
            C.Delay(2)
    C.Delay(3)
    Driver.CloseBrowser()




#browserDriver = Driver.get_Browser("edge")
#Driver().Initialize(browserDriver)
#GoogleLogin.GoAndLogGoogleSite(Sites.DRIVE)
#isTrue = TC104()
#print(isTrue)
