import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Base.Driver import Driver
import time

class CommonFunction(Driver):

    def Delay(seconds):
        CommonFunction.LogInfo("Waiting seconds: " + str(seconds))
        time.sleep(seconds)   
    
    def WaitElementBePresent(strategy, by, time = 10):
        CommonFunction.LogInfo("Waiting element to be Clickable, element"+ str(by) + " ...")
        try:
            element = WebDriverWait(Driver.get_Instance(), time).until(EC.element_to_be_clickable((strategy, by)))
            CommonFunction.LogInfo("Element found: "+ str(element))
        except NoSuchElementException:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))

    def SendKey(strategy, by, text):
        CommonFunction.LogInfo("Sending keys: "+ str(text) +" - In the element: "+ str(by) + " ...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            element = CommonFunction.FindElement(strategy, by)
            element.send_keys(text)
            CommonFunction.Delay(1)
            CommonFunction.LogInfo("Key sent to element: "+ str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))

    def FindElement(strategy, by):
        try:
            CommonFunction.LogInfo("Looking for element: " + str(by) + " ...")
            element = Driver.get_Instance().find_element(strategy, by)
            CommonFunction.LogInfo("Element found: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))
        
        return element
    
    def Click(strategy, by):
        CommonFunction.LogInfo("Clicking element...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            element = CommonFunction.FindElement(strategy, by)
            element.click()
            CommonFunction.LogInfo("Element clicked: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))

    def GoToSite(url):
        CommonFunction.LogInfo("Going to site: "+ url)
        Driver.get_Instance().get(url)

    def DoesElementExist(strategy, by):
        exist = None



#Driver().Initialize(Browser.CHROME)
#Driver.get_Instance().get("https://yahoo.com")


