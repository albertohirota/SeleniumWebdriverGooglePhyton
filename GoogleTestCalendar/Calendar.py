import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Base.Driver import Browser
from GoogleFramework.Base.GoogleLogin import GoogleLogin
from GoogleFramework.Base.GoogleLogin import Sites

#import clr, System
#from System import String
#from System.Collections import *
#sys.path.append("C:\\Users\\alber\\source\\repos\\SeleniumWebdriverPhyton\\SeleniumWebdriverPhyton\\GoogleFramework\\Base\\GoogleLogin.dll")
#clr.AddReference("GoogleLogin.dll")
#from Login import GoogleLogin


def Main():
    print("Test")
    
def TC201():
    print("Test1")
    tes = Driver()
    tes.Initialize(Browser.CHROME)

    ddd = GoogleLogin()
    ddd.GoToGoogleSite(Sites.CALENDAR,tes.Instance)

    #tes.Instance.get("http://www.yahoo.com")
    









TC201()



