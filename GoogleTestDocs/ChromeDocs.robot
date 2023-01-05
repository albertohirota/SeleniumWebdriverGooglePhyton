*** Settings ***
Library    SeleniumLibrary
Library    Docs.py      

Test Setup        SetupDocs    ${browser}
Test Teardown     DocsCleanUp


*** Variables ***
${browser}    chrome



*** Test Cases ***
TC301_ValidateFileExist
    ${value}    TC301
    Should Be True   ${Value}

TC302_ValidateNewFileCreated
    ${value}    TC302
    Should Be True   ${Value}

TC303_ValidateDocBody
    ${value}    TC303
    Should Be True   ${Value}

TC304_ValidateDocHeaders
    ${value}    TC304
    Should Be True   ${Value}

TC305_ValidateDocBodyNewText
    ${value}    TC305
    Should Be True   ${Value}



*** Keywords ***


