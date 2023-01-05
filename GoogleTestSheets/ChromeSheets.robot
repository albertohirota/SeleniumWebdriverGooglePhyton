*** Settings ***
Library    SeleniumLibrary
Library    Sheets.py      

Test Setup        SetupSheets    ${browser}
Test Teardown     SheetsCleanUp


*** Variables ***
${browser}    chrome



*** Test Cases ***
TC401_ValidateFileExist
    ${value}    TC401
    Should Be True   ${Value}

TC402_ValidateNewFileCreated
    ${value}    TC402
    Should Be True   ${Value}

TC403_ValidateSpreadsheetBodyInCellB1
    ${value}    TC403
    Should Be True   ${Value}

TC404_ValidateSheetcBodyTextInNewFile
    ${value}    TC404
    Should Be True   ${Value}


*** Keywords ***


