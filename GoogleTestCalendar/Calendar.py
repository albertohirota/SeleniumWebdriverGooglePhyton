import sys
sys.path.insert(0,"..")
from GoogleFramework.Base.Driver import Driver
from GoogleFramework.Base.Driver import Browser

def Main():
    print("Test")
    Driver.Initialize(Browser.CHROME)
