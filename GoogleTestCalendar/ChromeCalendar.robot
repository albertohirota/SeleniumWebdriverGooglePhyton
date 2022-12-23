*** Settings ***
Library    SeleniumLibrary
Library    Calendar.py      

Test Setup        SetupCalendar    ${browser}
Test Teardown     CalendarCleanUp


*** Variables ***
${browser}    chrome



*** Test Cases ***
TC201_ValidatenewCalendarEvent
    ${value}    TC201
    Should Be True   ${Value}

TC202_ValidateCalendarTextBody
    ${value}    TC202
    Should Be True   ${Value}

TC203_ValidateUserGuest
    ${value}    TC203
    Should Be True   ${Value}

*** Keywords ***




