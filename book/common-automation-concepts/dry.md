---
layout: default
---
# DRY - Don't Repeat Yourself

Throughout this book you may come across instances where we use the acronym DRY.
DRY means don't repeat yourself. It is a common programming practice that reduces the amount of
code and the complexity involved. Once you have invented the wheel, you might as well use it as
much as you can.

## Example

Two browser tests both log in before they check something else. Each test repeats the same
four lines:

```python
from selenium.webdriver.common.by import By

def test_admin_can_open_settings(browser):
    browser.get("https://example.com/login")
    browser.find_element(By.ID, "username").send_keys("admin")
    browser.find_element(By.ID, "password").send_keys("secret")
    browser.find_element(By.ID, "submit").click()
    browser.get("https://example.com/settings")
    assert browser.title == "Settings"

def test_admin_can_open_reports(browser):
    browser.get("https://example.com/login")
    browser.find_element(By.ID, "username").send_keys("admin")
    browser.find_element(By.ID, "password").send_keys("secret")
    browser.find_element(By.ID, "submit").click()
    browser.get("https://example.com/reports")
    assert browser.title == "Reports"
```

Move the repeated steps into one helper function, and both tests read the same way:

```python
from selenium.webdriver.common.by import By

def log_in_as_admin(browser):
    browser.get("https://example.com/login")
    browser.find_element(By.ID, "username").send_keys("admin")
    browser.find_element(By.ID, "password").send_keys("secret")
    browser.find_element(By.ID, "submit").click()

def test_admin_can_open_settings(browser):
    log_in_as_admin(browser)
    browser.get("https://example.com/settings")
    assert browser.title == "Settings"

def test_admin_can_open_reports(browser):
    log_in_as_admin(browser)
    browser.get("https://example.com/reports")
    assert browser.title == "Reports"
```

If the login page changes, you now update one function instead of every test.

## When not to DRY

Repetition in tests is not always bad. If a test is hard to read because it hides too much in a
helper, a few repeated lines may be the better choice. Aim for tests a newcomer can follow
without jumping between files.
