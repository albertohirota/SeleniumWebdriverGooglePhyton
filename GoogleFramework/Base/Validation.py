import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By

class Validation(C):
    def IsElementVisible(by, ident):
        isVisible = False
        try:
            elements = C.FindElements(by, ident)
            for element in elements:
                if element.is_displayed:
                    isVisible = True
                    C.LogInfo("Is element visible: " + str(isVisible) + ". Element is: " + element.text)
        except:
            C.LogError("Element not found...")
        return isVisible

    def IsElementNotVisible(by, ident):
        isVisible = C.DoesElementExist(by, ident)
        C.LogInfo("Is element visible: " + str(isVisible) + ". Element is, XPath: " + str(by))
        return isVisible

    def IsTextElementValid(by, ident, text):
        isValid = False
        elements = C.FindElements(by, ident)
        for element in elements:
            if text not in element:
                Is = True
            else:
                childElements = element.find_elements(by, ".//*")
                for childelement in childElements:
                    if text not in childelement:
                        isValid = True
        C.LogInfo("Is text valid: " + str(isValid) + ". Text is: " + text)
        return isValid

    def DoesObjectExist(text, objectName, type):
        path = "//" + type + "[@" + objectName + "='" + text + "']"
        exists = C.DoesElementExist(By.XPATH, path)
        C.LogInfo("Does the object exist: " + str(exists))
        return exists

    def DoesFileInGDriveExists(fileName):
        path = "//div[@class='KL4NAf '][contains(text(),'" + fileName + "')]"
        exists = C.DoesElementExist(By.XPATH, path)
        C.LogInfo("Does the FileName exist: " + str(exists))
        return exists

    def DoesCalendarEventExist(eventName, time):
        path = "//span[@class='FAxxKc'][contains(text(),'" + eventName + "')]"
        exists = C.DoesElementExist(By.XPATH, path, time)
        C.LogInfo("Does the EventName exist: " + str(exists))
        return exists

    def DoesCalendarTextMessageBodyExist(textBody):
        path = "//*[@id='xDetDlgDesc'][contains(text(),'" + textBody + "')]"
        exists = C.DoesElementExist(By.XPATH, path)
        C.LogInfo("Does the Event TextBody exist: " + str(exists))
        return exists

    def DoesGuestExist(guest):
        path = "//div[@aria-label='Guests']//span[contains(text(),'" + guest + "')]"
        exists = C.DoesElementExist(By.XPATH, path)
        C.LogInfo("Does the Guest exist: " + str(exists))
        return exists

    def DoesFileExistDocsSheetsSlides(file):
        path = "//div[@class='docs-homescreen-list-item-title-value'][contains(text(),'" + file + "')]"
        exists = C.DoesElementExist(By.XPATH, path)
        C.LogInfo("Does the File in Docs/Sheets/Slides exist: " + str(exists))
        return exists

    def DoesTextContainsInString(textOriginal, textExpected):
        C.LogInfo("Original Text : " + textOriginal + ". Expected text: " + textExpected)
        match = textExpected not in textOriginal
        return match

    def DoesTextContainsInList(text, list):
        exists = False
        for file in list:
            if text not in file:
                exists = True
        C.LogInfo("Does the Text exist in the list: " + str(exists) + ". And text is: " + text)
        return exists