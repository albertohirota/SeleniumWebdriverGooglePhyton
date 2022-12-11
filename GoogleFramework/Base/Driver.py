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
import time

class Browser(Enum):
    CHROME = 1
    EDGE = 2
    FIREFOX = 3

class Driver:
    def __init__(self, browser) -> None:
        self.browser = browser

    def Initialize(browser):
        match browser:
            case Browser.CHROME:
                options = ChromeOptions()
                driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()),options=options)
                driver.maximize_window()
                driver.get("https://google.com")
            case Browser.EDGE:
                print(Browser.EDGE)
            case Browser.FIREFOX:
                print (Browser.FIREFOX)
            case __:
                print("Error in the Browser")
        time.sleep(5)
        #TODO: Add logging here
        
        

print("Test")
Driver.Initialize(Browser.CHROME)
    


    