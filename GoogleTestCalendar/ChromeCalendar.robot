*** Settings ***
Library  SeleniumLibrary
Test Setup
Test Teardown


*** Variables ***


*** Test Cases ***
TC201_ValidatenewCalendarEvent
    Create Webdriver    chrome    executable_path:""    
    Open Browser    https://google.com/    chrome
    


*** Keywords ***


