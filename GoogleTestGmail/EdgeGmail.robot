*** Settings ***
Library    SeleniumLibrary
Library    Gmail.py      

Test Setup        SetupGmail    ${browser}
Test Teardown     GmailCleanUp


*** Variables ***
${browser}    edge



*** Test Cases ***
TC001_ValidateSendButtonIsDisplayed
    ${value}    TC001
    Should Be True   ${Value}

TC002_ValidateNewMessageText
    ${value}    TC002
    Should Be True   ${Value}

TC003_CancelEmailAndValidateNewEmailDoesNotExist
    ${value}    TC003
    Should Not Be True   ${Value}

TC004_ValidateBcc()
    ${value}    TC004
    Should Be True   ${Value}

TC005_ValidateReplyAllButtonIsDisplayed
    ${value}    TC005
    Should Be True   ${Value}

TC006_ValidateReplyPage
    ${value}    TC006
    Should Be True   ${Value}

TC007_ValidateForwardAndSendEmail
    ${value}    TC007
    Should Be True   ${Value}

*** Keywords ***



