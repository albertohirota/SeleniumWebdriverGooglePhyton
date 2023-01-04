import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from Screenshot import Screenshot
from datetime import datetime
from Base.Driver import Driver
import time
import config

class CommonFunction(Driver):

    def Delay(seconds):
        CommonFunction.LogInfo("Waiting seconds: " + str(seconds))
        time.sleep(seconds)   
    
    def WaitElementBePresent(by, ident, time = 10):
        CommonFunction.LogInfo("Waiting element to be Clickable, element"+ str(ident) + " ...")
        try:
            element = WebDriverWait(Driver.get_Instance(), time).until(EC.element_to_be_clickable((by, ident)))
            CommonFunction.LogInfo("Element found: "+ str(element))
        except NoSuchElementException:
            CommonFunction.LogWarn("NoSuchElement, Element NOT FOUND: "+ str(ident))
        except TimeoutException:
            CommonFunction.LogWarn("TimeOut, Element NOT FOUND: "+ str(ident))
        except Exception:
            CommonFunction.LogWarn("Exception, Element NOT FOUND: "+ str(ident))

    def WaitElementNotBePresent(by, ident, time = 10):
        CommonFunction.LogInfo("Waiting element not be present...")
        try:
            WebDriverWait(Driver.get_Instance(), time).until_not(EC.element_to_be_clickable((by, ident)))
            CommonFunction.LogInfo("Element no longer available")
        except TimeoutException:
            CommonFunction.LogError("Element still available: "+ str(ident))       

    def SendKey(by, ident, text):
        CommonFunction.LogInfo("Sending keys: "+ str(text) +" - In the element: "+ str(ident) + " ...")
        try:
            CommonFunction.WaitElementBePresent(by, ident)
            if CommonFunction.DoesElementExist:
                element = CommonFunction.FindElement(by, ident)
                element.send_keys(text)
                CommonFunction.Delay(1)
                CommonFunction.LogInfo("Key sent to element: "+ str(element))
            else:
                CommonFunction.LogError("Element does NOT exist")
        except:
            CommonFunction.LogError("Sendkey ERROR, verify: "+ str(ident))

    def FindElement(by, ident):
        try:
            CommonFunction.LogInfo("Looking for element: " + str(ident) + " ...")
            element = Driver.get_Instance().find_element(by, ident)
            CommonFunction.LogInfo("Element found: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(ident))
        
        return element
    
    def FindElements(by, ident):
        CommonFunction.LogInfo("Finding elements...")
        try:
            elements = Driver.get_Instance().find_elements(by, ident)
            CommonFunction.LogInfo("Elements found: " + len(elements))
        except:
            CommonFunction.LogWarn("Elements ERROR: "+ str(ident)) 
        return elements   

    def Click(by, ident):
        CommonFunction.LogInfo("Clicking element...")
        try:
            CommonFunction.WaitElementBePresent(by, ident)
            action = ActionChains(Driver.get_Instance())
            element = CommonFunction.FindElement(by, ident)
            action.click(on_element=element).perform()
            CommonFunction.LogInfo("Element clicked: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(ident))
    def RightClick(by, ident):
        CommonFunction.LogInfo("Right clicking element...")
        try:
            CommonFunction.WaitElementBePresent(by, ident)
            action = ActionChains(Driver.get_Instance())
            element = CommonFunction.FindElement(by, ident)
            action.context_click(on_element=element).perform()
            CommonFunction.LogInfo("Element right-clicked: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(ident))
    
    def Click_Parent(by, ident):
        CommonFunction.LogInfo("Clicking Parent element...")
        try:
            CommonFunction.WaitElementBePresent(by, ident)
            action = ActionChains(Driver.get_Instance())
            element = CommonFunction.FindElement(by, ident)
            parent = element.find_element(by, "./..")
            action.click(on_element=parent).perform()
            CommonFunction.LogInfo("Element right-clicked: " + str(element))
        except:
            CommonFunction.LogError("Element NOT FOUND: "+ str(ident))

    def GoToPage(url):
        CommonFunction.LogInfo("Going to site: "+ url)
        config.Instance.get(url)

    def DoesElementExist(by, ident, time = 10):
        CommonFunction.LogInfo("Checking if the element exists...")
        CommonFunction.WaitElementBePresent(by, ident, time)
        elements = CommonFunction.FindElements(by, ident)
        doesExist = (len(elements)>0)
        return doesExist

    def GetScreenshot(screenShotName):
        CommonFunction.LogInfo("Taking screenshot...")
        ticks = (datetime.utcnow() - datetime(1,1,1)).total_seconds() * 10000000
        fileName="sShot-"+screenShotName+"_"+ ticks + ".png"
        path = "C:\\Temp\\"+fileName+".png"
        Driver.get_Instance().save_screenshot(path)
        CommonFunction.LogInfo("ScreenShot taken: " + path)

    def SendKeyActionBuilder(by, ident, text):
        CommonFunction.LogInfo("Sending Key using Action builder...")
        try:
            CommonFunction.WaitElementBePresent(by, ident)
            if CommonFunction.DoesElementExist:
                action = ActionChains(Driver.get_Instance())
                element = CommonFunction.FindElement(by, ident)
                action.click(on_element=element)
                action.send_keys(text).perform()
                CommonFunction.Delay(1)
                CommonFunction.LogInfo("Key sent to element: "+ str(element))
            else:
                CommonFunction.LogError("Element does NOT exist")
        except:
            CommonFunction.LogError("Sendkey ERROR, verify: "+ str(ident))
    
    def SendKeyAndEnter(by, ident, text):
        CommonFunction.LogInfo("Sending Key and pressing Enter...")
        CommonFunction.WaitElementBePresent(by, ident)
        if CommonFunction.DoesElementExist:
            element = CommonFunction.FindElement(by, ident)
            element.send_keys(text)
            element.send_keys(Keys.ENTER)
            CommonFunction.Delay(1)
            CommonFunction.LogInfo("Key sent to element: "+ str(element) + " And the text: " + str(text))
        else:
            CommonFunction.LogError("Element does NOT exist")

    def ClearTextElement(by, ident):
        CommonFunction.LogInfo("Clear element, send text and press Enter...")
        try:
            CommonFunction.WaitElementBePresent(by, ident)
            if CommonFunction.DoesElementExist:
                element = CommonFunction.FindElement(by, ident)
                element = CommonFunction.FindElement(by, ident)
                element.send_keys(Keys.CONTROL+"a")
                element.send_keys(Keys.DELETE)
                CommonFunction.Delay(2)
                CommonFunction.LogInfo("Key sent to element: "+ str(element))
            else:
                CommonFunction.LogError("Element does NOT exist")
        except:
            CommonFunction.LogError("Sendkey ERROR, verify: "+ str(ident))

    def SwitchToDefaultContent():
        Driver.get_Instance().switch_to.default_content()

    def SwitchFrame(by, ident):
        CommonFunction.LogInfo("Switching frame...")
        Driver.get_Instance().switch_to.parent_frame()
        CommonFunction.SwitchToDefaultContent()
        Driver.get_Instance().switch_to.frame(by, ident)

    def GetTextFromElement(by, ident):
        CommonFunction.WaitElementBePresent(by, ident)
        text = Driver.get_Instance().find_element(by, ident).text
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
        CommonFunction.LogInfo("Closing browser tab: " + str(tab))
    
    def GoToTab(tab):
        CommonFunction.LogInfo("Going to Tab: " + str(tab) + " ...")
        Driver.get_Instance().switch_to.window(tab)
        CommonFunction.LogInfo("Going to tab: " + str(tab))

    def IsElementVisible(by, ident):
        CommonFunction.LogInfo("Checking if elenent is visible...")
        isDisplayed = None
        try:
            element = CommonFunction.FindElement(by, ident)
            isDisplayed = True if element.is_displayed else False
            CommonFunction.LogInfo("Elements isDisplaued: " + str(isDisplayed))
        except:
            CommonFunction.LogError("Elements ERROR: "+ str(ident))         
        return isDisplayed


#browserDriver = Driver.get_Browser("chrome")
#Driver.Instance = Driver().Initialize(browserDriver)
#Driver.get_Instance().get("https://yahoo.com")


