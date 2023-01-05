import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By
from GoogleFramework.Base.GoogleApi import GoogleApi as GApi

class SlidesPage(C):
    PresentationArea = "//*[@id='editor-i0']"
    
    def SendText_PresentationBody(text): C.SendKeyActionBuilder(By.XPATH, SlidesPage.PresentationArea, text)

    def GetSlideObject(share):
        C.LogInfo("Getting Google Sheets spreadshet")
        service = GApi.GetSlidesService(share)
        SlideId = GApi.GetCurrentGoogleDocID("slides")
        request = service.presentations().get(presentationId=SlideId).execute()
        presentation = request.get('slides')
        return presentation
        
    def GetSlidesTexts(share = False):
        C.LogInfo("Getting Presentation Texts")
        presentationTexts = []
        C.Delay(4)
        obj = SlidesPage.GetSlideObject(share)
        for slidesObject in obj:
            for elementsName, elementsValues in slidesObject.items():    
                if str(elementsName) == "pageElements":
                    for element in elementsValues:                    
                        for elementName, elementValue in element.items():
                            if str(elementName) == "shape":
                                for textName, textValue in elementValue.items():
                                    if str(textName) == "text":
                                        for textElementName, textElementValue in textValue.items():
                                            if str(textElementName) == "textElements":
                                                for textRun in textElementValue:
                                                    for textRunName, textRunValue in textRun.items():
                                                        if str(textRunName) == "textRun":
                                                            for contentName, contentValue in textRunValue.items():
                                                                if str(contentName) == "content":
                                                                    presentationTexts.append(contentValue)
                                                                    print("Value: "+str(contentValue))
                
        return presentationTexts



