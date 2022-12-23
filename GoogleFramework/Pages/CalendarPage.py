import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By


class CalendarPage(C):
    Create = "//div[@class='mr0WL'][contains(text(),'Create')]"
    Event = "//div[@class='jO7h3c'][contains(text(),'Event')]"
    AddTitleSummaryPage = "//input[@aria-label='Add title']"
    ButtonSaveSummaryPage = "//span[contains(text(),'Save')]"
    ButtonDeleteSummaryPage = "//div[@aria-label='Delete event']"
    ButtonMoreOptionsSummaryPage = "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf LjDxcd XhPA0b LQeN7 nYqxP']"
    AddTextCalendarBody = "//div[@aria-label='Description']"
    AddGuest = "//input[@aria-label='Guests']"
    ButtonSave = "//input[@aria-label='Title']/following::span[text()='Save'][1]"
    ButtonSend = "//div[@role='button']/following::span[text()='Send']"
    IconCloseSummaryPage = "//div[@aria-label='Close']"

    def Click_Create(): C.Click(By.XPATH, CalendarPage().Create)
    def Click_Event():  C.Click(By.XPATH, CalendarPage().Event)
    def Click_ButtonSaveSummaryPage(): C.Click(By.XPATH,CalendarPage().ButtonSaveSummaryPage)
    def Click_ButtonSave(): C.Click(By.XPATH,CalendarPage().ButtonSave)
    def Click_ButtonDeleteSummaryPage(): C.Click(By.XPATH,CalendarPage().ButtonDeleteSummaryPage)
    def Click_IconCloseSummaryPage(): C.Click(By.XPATH,CalendarPage.IconCloseSummaryPage)
    def Click_ButtonMoreOptionsSummaryPage(): C.Click(By.XPATH,CalendarPage.ButtonMoreOptionsSummaryPage)
    def Add_TextCalendarBody(text): C.SendKey(By.XPATH,CalendarPage.AddTextCalendarBody, text)
    def Add_Title_SummaryPage(title): C.SendKey(By.XPATH,CalendarPage.AddTitleSummaryPage, title)
    def Add_Guest(guest): C.SendKeyAndEnter(By.XPATH,CalendarPage.AddGuest, guest)

    def CreateNewEvent():
        C.LogInfo("Creating new event...")
        CalendarPage.Click_Create()
        C.Delay(2)
        CalendarPage.Click_Event()
        C.WaitElementBePresent(By.XPATH, CalendarPage.AddTitleSummaryPage)

    def Click_ExistingEvent(ev):
        C.LogInfo("Clicking an existing Event: "+ str(ev))
        by = "//span[@class='FAxxKc'][contains(text(),'" + str(ev) + "')]"
        C.WaitElementBePresent(By.XPATH, by,15)
        C.Click_Parent(By.XPATH, by)
        if not C.DoesElementExist(By.XPATH, CalendarPage.ButtonDeleteSummaryPage):
            C.Click_Parent(By.XPATH, "//span[@class='FAxxKc'][contains(text(),'" + str(ev) + "')]")

    def DeleteEvent(ev):
        C.LogInfo("Deleting event: "+ str(ev))
        CalendarPage.Click_ExistingEvent(ev)
        C.Delay(2)
        CalendarPage.Click_ButtonDeleteSummaryPage()

    def Click_ButtonSend():
        if C.IsElementVisible(By.XPATH, CalendarPage.ButtonSend):
            C.Click(By.XPATH, CalendarPage.ButtonSend)