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
    Instance = None

    def __init__(self):
        pass

    def Initialize(self, browser):
        match browser:
            case Browser.CHROME:
                options = ChromeOptions()
                driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()),options=options)
                self.Instance = driver
            case Browser.EDGE:
                options = EdgeOptions()
                driver = webdriver.Edge(service=EdgeServices(EdgeChromiumDriverManager().install()),options=options)
                self.Instance = driver
            case Browser.FIREFOX:
                options = FirefoxOptions()
                driver = webdriver.Firefox(service=FirefoxServices(GeckoDriverManager().install()),options=options)
                self.Instance = driver
            case __:
                print("Error in the Browser")

        self.Instance.maximize_window()
        self.Instance.implicitly_wait(10)
        #TODO: Add logging here
    
    def CloseBrowser(self):
        self.Instance.close()
        # TODO add log
    
    def InstanceClose(self):
        self.Instance.quit()
        # TODO add Log
        

#test = Driver()
#test.Initialize(Browser.CHROME)
#rr = test.Instance




    


    