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
import logging

logging.basicConfig(
    filename='C:\\temp\\Logs.log', 
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%Y/%m/%d %I:%M:%S %p',
    encoding='utf-8',
    level=logging.INFO)

Instance = None

class Browser(Enum):
    CHROME = 1
    EDGE = 2
    FIREFOX = 3

class Driver:

    def __init__(self):
        pass
    
    def get_Instance():
        return Instance

    def Initialize(self, browser):
        global Instance
        match browser:
            case Browser.CHROME:
                options = ChromeOptions()
                driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()),options=options)
                Instance = driver
            case Browser.EDGE:
                options = EdgeOptions()
                driver = webdriver.Edge(service=EdgeServices(EdgeChromiumDriverManager().install()),options=options)
                Instance = driver
            case Browser.FIREFOX:
                options = FirefoxOptions()
                driver = webdriver.Firefox(service=FirefoxServices(GeckoDriverManager().install()),options=options)
                Instance = driver
            case __:
                print("Error in the Browser")

        Instance.maximize_window()
        Instance.implicitly_wait(10)
        Driver.LogInfo("Browser should be opened: "+str(browser))
           
    def CloseBrowser(self):
        Instance.close()
        Driver.LogInfo("Browser Closed")
    
    def InstanceClose(self):
        Instance.quit()
        Driver.LogInfo("Instance Quit")

    def LogInfo(text):
        logging.info(text)

    def LogWarn(text):
        logging.warning(text)

    def LogError(text):
        logging.error(text)

        

#test = Driver()
#test.Initialize(Browser.CHROME)
#Instance.get("https://google.com")





    


    