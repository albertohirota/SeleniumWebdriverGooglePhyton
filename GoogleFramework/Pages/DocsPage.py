import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By
from GoogleFramework.Base.GoogleApi import GoogleApi as GApi

class DocsPage(C):
    ContentArea = "//canvas[@class='kix-canvas-tile-content']"
    def SendText_DocumentBody(text): C.SendKeyActionBuilder(By.XPATH, DocsPage.ContentArea,text)

    def GetDocumentObject(share):
        C.LogInfo("Getting Document Object")
        service = GApi.GetDocsService(share)
        C.Delay(3)
        DocId = GApi.GetCurrentGoogleDocID("docs")
        request = service.documents().get(documentId=DocId).execute()
        return request

    def GetDocumentHeader(share = False): 
        C.LogInfo("Getting Document Header")
        headerListReturn = []
        docObject = DocsPage.GetDocumentObject(share)
        for headerName, headerValue in docObject.items():
            if str(headerName) == "headers":
                for kix in headerValue.values():
                    for contentName, contentValue in kix.items():
                        if str(contentName) == "content":
                            for paragraph in contentValue:
                                for paragraphName, paragraphValue in paragraph.items():
                                    if str(paragraphName) == "paragraph":
                                        for elementName, elementValue in paragraphValue.items():
                                            if str(elementName) == "elements":
                                                for textRun in elementValue:
                                                    for textRunName, textRunValue in textRun.items():
                                                        if str(textRunName) == "textRun":
                                                            for cName, cValue in textRunValue.items():
                                                                if str(cName) == "content":  
                                                                    headerListReturn.append(cValue)
        return headerListReturn

    def GetDocumentBody(share = False):
        C.LogInfo("Getting Document body")
        bodyReturn = []
        docObject = DocsPage.GetDocumentObject(share)
        for bodyName, bodyValue in docObject.items():
            if str(bodyName) == "body":
                for contentName, contentValue in bodyValue.items():
                    if str(contentName) == "content":
                        for paragraph in contentValue:
                            for paragraphName, paragraphValue in paragraph.items():
                                if str(paragraphName) == "paragraph":
                                    for elementName, elementValue in paragraphValue.items():
                                        if str(elementName) == "elements":
                                            for textRun in elementValue:
                                                for textRunName, textRunValue in textRun.items():
                                                    if str(textRunName) == "textRun":
                                                        for cName, cValue in textRunValue.items():
                                                            if str(cName) == "content":
                                                                bodyReturn.append(cValue)
        return bodyReturn

    
           