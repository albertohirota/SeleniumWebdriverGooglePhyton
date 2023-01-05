import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By
from GoogleFramework.Base.GoogleApi import GoogleApi as GApi

class DocsPage(C):
    C.Delay(2)