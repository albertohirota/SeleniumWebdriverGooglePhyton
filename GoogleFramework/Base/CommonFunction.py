import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.Driver import Driver
import time
from Base.Driver import Browser


class CommonFunction(Driver):

    def LogInfo(text):
        super().logging.info(text)

    def LogWarn(text):
        super().logging.warning(text)

    def LogError(text):
        super().logging.error(text)

    def Delay(seconds):
        CommonFunction.LogInfo("Waiting seconds: " + str(seconds))
        time.sleep(seconds)   
    
    def WaitElementBePresent(by, time = 10):
        CommonFunction.LogInfo("Waiting element be Clickable, element"+ str(by) + " ...")
        element = WebDriverWait(Driver.get_Instance(), time).until(EC.element_to_be_clickable((By.XPATH, by)))
        CommonFunction.LogInfo("Element found: "+ str())
        return element

    def SendKey(by, text):
        CommonFunction.LogInfo("Sending keys: "+ text +" - In the element: "+ str(by) + " ...")
        element = CommonFunction.WaitElementBePresent(by)
        element.send_keys(text)
        CommonFunction.Delay(1)
        CommonFunction.LogInfo("Key sent")

    def FindElement(by):
        try:
            CommonFunction.LogInfo("Looking for element: " + str(by) + " ...")
            element = Driver.get_Instance().find_element(by)
            CommonFunction.LogInfo("Element found: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))
        
        return element
    
    def Click(by):
        CommonFunction.LogInfo("Clicking element...")
        element = CommonFunction.WaitElementBePresent(by)
        element.click()

    def GoToSite(url):
        CommonFunction.LogInfo("Going to site: "+ url)
        Driver.get_Instance().get(url)


#Driver().Initialize(Browser.CHROME)
#Driver.get_Instance().get("https://yahoo.com")


