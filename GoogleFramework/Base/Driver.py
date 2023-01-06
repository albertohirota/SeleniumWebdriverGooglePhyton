import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeServices
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxServices
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager 
from enum import Enum


class Browser(Enum):
    CHROME = 1
    EDGE = 2
    FIREFOX = 3

class Driver:

    @staticmethod
    def get_Instance():
        return config.Instance

    @staticmethod
    def set_Instance(instance):
        config.Instance = instance

    def get_Browser(browser):
        match browser.lower():
            case "chrome":
                return Browser.CHROME
            case "edge":
                return Browser.EDGE
            case "firefox":
                return Browser.FIREFOX
            case __:
                Driver.LogError("Browser could not be identified")
                return Browser.CHROME

    def Initialize(self, browser):
        global Instance
        match browser:
            case Browser.CHROME:
                options = ChromeOptions()
                driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()),options=options)
                Driver.set_Instance(driver)
            case Browser.EDGE:
                options = EdgeOptions()
                driver = webdriver.Edge(service=EdgeServices(EdgeChromiumDriverManager().install()),options=options)
                Driver.set_Instance(driver)
            case Browser.FIREFOX:
                options = FirefoxOptions()
                driver = webdriver.Firefox(service=FirefoxServices(GeckoDriverManager().install()),options=options)
                Driver.set_Instance(driver)
            case __:
                Driver.LogError("Error in the Browser")

        config.Instance.maximize_window()
        config.Instance.implicitly_wait(10)
        Driver.LogInfo("Browser should be opened: "+str(browser))
           
    def CloseBrowser():    
        config.Instance.close()
        Driver.InstanceClose()
        Driver.LogInfo("Browser Closed")
    
    def InstanceClose():
        config.Instance.quit()
        Driver.LogInfo("Instance Quit")

    def LogInfo(text):
        config.logging.info(text)

    def LogWarn(text):
        config.logging.warning(text)

    def LogError(text):
        config.logging.error(text)



#test = Driver()
#test.Initialize(Browser.CHROME)
#Instance.get("https://google.com")





    


    