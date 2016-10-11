*** Settings ***
Documentation     Example Gherkin Style Test

Library    AdderLibrary.py

*** Test Cases ***
Addition
    Given two numbers "3" and "5"
    Then total of result is "8"

*** Keywords ***
two numbers "${a}" and "${b}"
    Add input    ${a}    ${b}
total of result is "${total}"
    Total    ${total}
