*** Settings ***
Library    SeleniumLibrary
Library    GDrive.py      

Test Setup        SetupGDrive    ${browser}
Test Teardown     GDriveCleanUp


*** Variables ***
${browser}    firefox



*** Test Cases ***
TC101_ValidateFileExists
    ${value}    TC101
    Should Be True   ${Value}

TC102_ValidateFileExistInShareWithMeFolder
    ${value}    TC102
    Should Be True   ${Value}

TC103_ValidateCreatingOfNewFile
    ${value}    TC103
    Should Be True   ${Value}

TC104_ValidateFileExistsThroughApi
    ${value}    TC104
    Should Be True   ${Value}


*** Keywords ***


