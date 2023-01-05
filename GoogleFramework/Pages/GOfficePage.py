import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Base.Driver import Driver

class GOfficePage(C): 
    DocumentTitle = "//input[@class='docs-title-input']"
    DocumentStatus = "//div[@aria-label='Document status: Saved to Drive.']"
    DocumentBlank = "//img[contains(@src,'blank')]"
    ButtonGoogle = "//*[@data-tooltip='Docs home' or @data-tooltip='Sheets home'or @data-tooltip='Slides home']"
    ButtonDeleteFromGoogleDocs = "//div[@class='docs-homescreen-overflowmenuitem-text'][contains(text(),'Remove')]"
    ButtonMoveToTrash = "//button[@name='moveToTrash']"
    ButtonShare = "//*[@id='docs-titlebar-share-client-button']"
    ButtonSharingSend = "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ nCP5yc AjY5Oe DuMIQc LQeN7 ftJYz']"
    ButtonSharing = "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ nCP5yc AjY5Oe DuMIQc LQeN7 xFWpbf oWBWHf ftJYz CZCFtc-bMElCd sj692e RCmsv jbArdc']"
    IframeSharing = "//iframe[@class='share-client-content-iframe']"
    TextBoxSharing = "//input[@class='zeumMd d2j1H']"
    CheckBoxNotify = "//input[@name='notify']"

    def Click_DocumentNameTitle(): C.Click(By.XPATH, GOfficePage.DocumentTitle)
    def Click_ButtonGoogle(): C.Click(By.XPATH, GOfficePage.ButtonGoogle)
    def Click_ButtonShare(): C.Click(By.XPATH, GOfficePage.ButtonShare)
    def Click_DocumentBlank(): C.Click(By.XPATH, GOfficePage.DocumentBlank)
    def Click_OpenFile(file): C.Click(By.XPATH, "//div[@class='docs-homescreen-list-item-title-value'][contains(text(),'" + file + "')]")
    def RightClick_File(fileName): C.RightClick(By.XPATH, "//div[@title='" + fileName + "']")

    def WaitDocumentBeingSaved():
        C.LogInfo("Waiting document being saved")
        fileSaved = C.DoesElementExist(By.XPATH, GOfficePage.DocumentStatus)
        while not fileSaved:
            fileSaved = C.DoesElementExist(By.XPATH, GOfficePage.DocumentStatus)

    def RenameDocumentName(documentName):
        C.LogInfo("Renaming Document to: "+ documentName)
        GOfficePage.Click_DocumentNameTitle()
        C.ClearTextElement(By.XPATH, GOfficePage.DocumentTitle)
        C.SendKeyAndEnter(By.XPATH, GOfficePage.DocumentTitle, documentName)
        GOfficePage.WaitDocumentBeingSaved()

    def NotifyPeopleInSharing(notify):
        C.LogInfo("Notify people: "+str(notify))
        selected = Driver.get_Instance().find_element(By.XPATH, GOfficePage.CheckBoxNotify).is_selected()
        if (selected != notify):
            C.SendKey(By.XPATH, GOfficePage.CheckBoxNotify, Keys.SPACE)

    def DeleteFile(fileName):
        C.LogInfo("Deleting file: "+ fileName)
        GOfficePage.RightClick_File(fileName)
        C.Click(By.XPATH, GOfficePage.ButtonDeleteFromGoogleDocs)
        C.Click(By.XPATH, GOfficePage.ButtonMoveToTrash)

    def AddSharedUser(user):
        C.LogInfo("Adding shared user: "+ user)
        C.SwitchFrame(By.XPATH, GOfficePage.IframeSharing)
        C.SendKeyAndEnter(By.XPATH, GOfficePage.TextBoxSharing,user)

    def Click_ButtonShareSend():
        exist = C.DoesElementExist(By.XPATH, GOfficePage.ButtonSharingSend)
        if exist:
            C.Click(By.XPATH, GOfficePage.ButtonSharingSend)
        else:
            C.Click(By.XPATH, GOfficePage.ButtonSharing)

    def Click_SendInSharingWindow():
        C.LogInfo("Sending in Sharing Window")
        C.Delay(3)
        GOfficePage.NotifyPeopleInSharing(False)
        GOfficePage.Click_ButtonShareSend()
        C.Delay(2)
        C.WaitElementNotBePresent(By.XPATH, GOfficePage.ButtonSharingSend)
        C.WaitElementNotBePresent(By.XPATH, GOfficePage.ButtonSharing)
        C.Delay(1)
        C.RefreshPage()
        C.Delay(2)
        C.SwitchToDefaultContent()
        C.Delay(3)

    
    def SharePublic(user):
        C.LogInfo("Sharing document with: "+ user)
        C.WaitElementBePresent(By.XPATH,GOfficePage.ButtonShare)
        GOfficePage.Click_ButtonShare()
        GOfficePage.AddSharedUser(user)
        GOfficePage.Click_SendInSharingWindow()



    
        
    