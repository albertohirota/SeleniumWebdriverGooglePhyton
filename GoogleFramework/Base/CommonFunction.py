import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from Screenshot import Screenshot
from datetime import datetime
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

    def WaitElementNotBePresent(strategy, by, time = 10):
        CommonFunction.LogInfo("Waiting element not be present...")
        try:
            WebDriverWait(Driver.get_Instance(), time).until_not(EC.element_to_be_clickable((strategy, by)))
            CommonFunction.LogInfo("Element no longer available")
        except TimeoutException:
            CommonFunction.LogError("Element still available: "+ str(by))       

    def SendKey(strategy, by, text):
        CommonFunction.LogInfo("Sending keys: "+ str(text) +" - In the element: "+ str(by) + " ...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            if CommonFunction.DoesElementExist:
                element = CommonFunction.FindElement(strategy, by)
                element.send_keys(text)
                CommonFunction.Delay(1)
                CommonFunction.LogInfo("Key sent to element: "+ str(element))
            else:
                CommonFunction.LogError("Element does NOT exist")
        except:
            CommonFunction.LogError("Sendkey ERROR, verify: "+ str(by))

    def FindElement(strategy, by):
        try:
            CommonFunction.LogInfo("Looking for element: " + str(by) + " ...")
            element = Driver.get_Instance().find_element(strategy, by)
            CommonFunction.LogInfo("Element found: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))
        
        return element
    
    def FindElements(strategy, by):
        CommonFunction.LogInfo("Finding elements...")
        try:
            elements = Driver.get_Instance().find_elements(strategy, by)
            CommonFunction.LogInfo("Elements found: " + len(elements))
        except:
            CommonFunction.LogError("Elements ERROR: "+ str(by)) 
        return elements   

    def Click(strategy, by):
        CommonFunction.LogInfo("Clicking element...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            #element = CommonFunction.FindElement(strategy, by)
            #element.click()
            action = ActionChains(Driver.get_Instance())
            element = CommonFunction.FindElement(strategy, by)
            action.click(on_element=element).perform()
            CommonFunction.LogInfo("Element clicked: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))
    def RightClick(strategy, by):
        CommonFunction.LogInfo("Right clicking element...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            action = ActionChains(Driver.get_Instance())
            element = CommonFunction.FindElement(strategy, by)
            action.context_click(on_element=element).perform()
            CommonFunction.LogInfo("Element right-clicked: " + str(element))
            # If start to fail, ActionBuilder or ActionChains may be required to install in this method
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))
    
    def Click_Parent(strategy, by):
        CommonFunction.LogInfo("Clicking Parent element...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            action = ActionChains(Driver.get_Instance())
            element = CommonFunction.FindElement(strategy, by)
            parent = element.find_element(strategy, "./..")
            action.click(on_element=parent).perform()
            CommonFunction.LogInfo("Element right-clicked: " + str(element))
            # If start to fail, ActionBuilder or ActionChains may be required to install in this method
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(by))

    def GoToPage(url):
        CommonFunction.LogInfo("Going to site: "+ url)
        Driver.get_Instance().get(url)

    def DoesElementExist(strategy, by):
        CommonFunction.LogInfo("Checking if the element exists...")
        CommonFunction.WaitElementBePresent(strategy, by)
        elements = CommonFunction.FindElements(strategy, by)
        doesExist = (len(elements)>0)
        return doesExist

    def GetScreenshot(screenShotName):
        CommonFunction.LogInfo("Taking screenshot...")
        ticks = (datetime.utcnow() - datetime(1,1,1)).total_seconds() * 10000000
        fileName="sShot-"+screenShotName+"_"+ ticks + ".png"
        path = "C:\\Temp\\"+fileName+".png"
        Driver.get_Instance().save_screenshot(path)
        CommonFunction.LogInfo("ScreenShot taken: " + path)

    def SendKeyActionBuilder(strategy, by, text):
        CommonFunction.LogInfo("Sending Key using Action builder...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            if CommonFunction.DoesElementExist:
                action = ActionChains(Driver.get_Instance())
                element = CommonFunction.FindElement(strategy, by)
                action.click(on_element=element)
                action.send_keys(text).perform()
                CommonFunction.Delay(1)
                CommonFunction.LogInfo("Key sent to element: "+ str(element))
            else:
                CommonFunction.LogError("Element does NOT exist")
        except:
            CommonFunction.LogError("Sendkey ERROR, verify: "+ str(by))
    
    def SendKeyAndEnter(strategy, by, text):
        CommonFunction.LogInfo("Sending Key and pressing Enter...")
        CommonFunction.WaitElementPresent(by)
        if CommonFunction.DoesElementExist:
            element = CommonFunction.FindElement(strategy, by)
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
            CommonFunction.Delay(1)
            CommonFunction.LogInfo("Key sent to element: "+ str(element) + " And the text: " + str(text))
        else:
            CommonFunction.LogError("Element does NOT exist")

    def ClearTextElement(strategy, by):
        CommonFunction.LogInfo("Clear element, send text and press Enter...")
        try:
            CommonFunction.WaitElementBePresent(strategy, by)
            if CommonFunction.DoesElementExist:
                element = CommonFunction.FindElement(strategy, by)
                element.send_keys(Keys.CONTROL+"a")
                element.send_keys(Keys.DELETE)
                CommonFunction.Delay(2)
                CommonFunction.LogInfo("Key sent to element: "+ str(element))
            else:
                CommonFunction.LogError("Element does NOT exist")
        except:
            CommonFunction.LogError("Sendkey ERROR, verify: "+ str(by))

    def SwitchFrame(strategy, by):
        CommonFunction.LogInfo("Switching frame...")
        Driver.get_Instance().switch_to.parent_frame()
        Driver.get_Instance().switch_to.default_content()
        Driver.get_Instance().switch_to.frame(strategy, by)

    def GetTextFromElement(strategy, by):
        CommonFunction.WaitElementBePresent(strategy, by)
        text = Driver.get_Instance().find_element(strategy, by).text
        CommonFunction.LogInfo("Getting text from element: " + text+" ...")
        CommonFunction.LogInfo("Text found: " + text)
        return text

    def RefreshPage():
        Driver.get_Instance().refresh()
        CommonFunction.LogInfo("Reloading browser")

    def CloseTab(tab):
        CommonFunction.LogInfo("Closing Tab: "+ str(tab)+" ...")
        Driver.get_Instance().window_handles[tab]
        Driver.get_Instance().close()
        CommonFunction.LogInfo("Closing browser tab: " + tab.ToString())
    
    def GoToTab(tab):
        CommonFunction.LogInfo("Going to Tab: " + str(tab) + " ...")
        Driver.get_Instance().switch_to.window(tab)
        CommonFunction.LogInfo("Going to tab: " + tab.ToString())


#Driver().Initialize(Browser.CHROME)
#Driver.get_Instance().get("https://yahoo.com")


