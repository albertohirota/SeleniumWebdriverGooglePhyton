import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from Base.Driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GmailPage(C):
    ButtonCompose = "//div[@class='T-I T-I-KE L3']"
    ButtonSend = "//*[@role='button' and text()='Send']"
    TitleEmail = "//*[@class='aYF']"
    ButtonDiscard = "//*[@aria-label='Discard draft ‪(Ctrl-Shift-D)‬']"
    CcBoxLabel = "//span[@class='aB gQ pE']"
    BccBoxLabel = "//span[@class='aB  gQ pB']"
    To = "//*[@name='to']//*[@name='to' or @class='agP aFw']"
    CcBox = "//*[@name='cc']//*[@name='cc' or @class='agP aFw']"
    BccBox = "//*[@name='bcc']//*[@name='bcc' or @class='agP aFw']"
    Subject = "//*[@name='subjectbox']"
    MessageBody = "//*[contains(@class,'Am Al editable LW-avf')]"
    InboxListNewEmail = "//tr[@class='zA zE']"
    ReadViewEmailBody = "//div[@class,'a3s aiL']"
    ButtonReply = "//span[@class='ams bkH']"
    ButtonReplyAll = "//span[text()='Reply all' and @role='link']"
    ButtonForward = "//span[text()='Forward' and @role='link']"
    FolderInbox = "//div[@data-tooltip='Inbox']"
    CheckBoxSelectAll = "//span[@class='T-Jo J-J5-Ji']"
    ButtonDelete = "//div[@data-tooltip='Delete']"

    def Click_NewEmail(): C.Click(By.XPATH, GmailPage().ButtonCompose)
    def Click_ButtonDiscard(): C.Click(By.XPATH, GmailPage().ButtonDiscard)
    def Click_SendEmail(): C.Click(By.XPATH, GmailPage().ButtonSend)
    def Click_ButtonReply(): C.Click(By.XPATH, GmailPage().ButtonReply)
    def Click_ButtonForward(): C.Click(By.XPATH, GmailPage().ButtonForward)
    def GoToInbox(): C.Click(By.XPATH, GmailPage().FolderInbox)
    def Click_CheckBoxSelectAll(): C.Click(By.XPATH, GmailPage().CheckBoxSelectAll)
    def Click_ButtonDelete(): C.Click(By.XPATH, GmailPage().ButtonDelete)

    def PopulateEmail(email, subject, messageBody, cc=None, bcc=None):
            C.LogInfo("Populating email...")
            C.Delay(2)
            C.SendKeyAndEnter(By.XPATH, GmailPage().To, email)

            if (cc != None):
                C.Click(By.XPATH, GmailPage().CcBoxLabel)
                C.SendKeyAndEnter(By.XPATH,GmailPage().CcBox, cc)
            if (bcc != None):
                C.Click(By.XPATH, GmailPage().BccBoxLabel)
                C.SendKeyAndEnter(By.XPATH, GmailPage().BccBox, bcc)

            C.SendKey(By.XPATH, GmailPage().Subject, subject)
            C.SendKey(By.XPATH, GmailPage().MessageBody, messageBody)

    def WaitAndOpenReceivedEmail(subject):
        C.LogInfo("Waiting to receive and Open email")
        C.Delay(2)
        emails = C.FindElements(By.XPATH, GmailPage().InboxListNewEmail)
        for newEmail in emails:
            if subject in newEmail.text:
                C.LogInfo("New email found: "+ str(newEmail))
                try:
                    action = ActionChains(Driver.get_Instance())
                    action.click(on_element=newEmail).perform()
                    C.Delay(2)
                except:
                    childs = C.FindElements(By.XPATH, ".//*")
                    for child in childs:
                        if subject in child.text: #or use child.text
                            action = ActionChains(Driver.get_Instance())
                            action.click(on_element=newEmail).perform()
                            C.Delay(2)
                break
                
