import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from Base.CommonFunction import CommonFunction as C
from selenium.webdriver.common.by import By
from GoogleFramework.Base.GoogleApi import GoogleApi as GApi

class GDrivePage(C):
    ButtonNewFile = "//span[contains(text(),'New')]"
    MenuGoogleDocs = "//div[@class='a-v-T'][contains(text(),'Google Docs')]"
    DeleteButtonFromGoogleDrive = "//div[@aria-label='Remove']"

    def Click_NewFile(): C.Click(By.XPATH, GDrivePage.ButtonNewFile)
    def Click_GoogleDocs(): C.Click(By.XPATH, GDrivePage.MenuGoogleDocs)
    def Click_DeleteIconFromGoogleDrive(): C.Click(By.XPATH, GDrivePage.DeleteButtonFromGoogleDrive)
    def Click_DriveMenuFolder(folder): C.Click(By.XPATH, "//span[@class='a-s-T'][contains(text(),'"+folder+"')]")
    def Click_FileInDrive(file): C.Click(By.XPATH, "//div[contains(@aria-label,'"+file+"')][contains(text(),'"+file+"')]")

    def DeleteFileInDrive(file):
        C.LogInfo("Deleting File in Drive, file: "+ file)
        GDrivePage.Click_FileInDrive(file)
        GDrivePage.Click_DeleteIconFromGoogleDrive()

    def GetDriveJson(share):
        C.LogInfo("Getting Google Drive Object")
        service = GApi.GetDriveService(share)
        result = service.files().list(fields="nextPageToken, files(id,name)").execute()
        files= result.get('files',[])
        return files
    
    def GetFileList(share = False):
        C.LogInfo("Getting Google Drive File List through API")
        fileList = []
        driveList = GDrivePage.GetDriveJson(share)
        for fileDic in driveList:
            for fileName, fileValue in fileDic.items():
                if str(fileName) == "name":
                    fileList.append(fileValue)
        return fileList