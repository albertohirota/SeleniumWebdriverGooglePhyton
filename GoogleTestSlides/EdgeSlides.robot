*** Settings ***
Library    SeleniumLibrary
Library    Slides.py      

Test Setup        SetupSlides    ${browser}
Test Teardown     SlidesCleanUp


*** Variables ***
${browser}    edge



*** Test Cases ***
TC501_ValidateFileExist
    ${value}    TC501
    Should Be True   ${Value}

TC502_ValidateNewFileCreated
    ${value}    TC502
    Should Be True   ${Value}

TC503_ValidateTextInThePresentation
    ${value}    TC503
    Should Be True   ${Value}

TC504_ValidateBodyTextInNewFile
    ${value}    TC504
    Should Be True   ${Value}

*** Keywords ***


