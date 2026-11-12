---
layout: default
---
# Lettuce + Selenium

This chapter drives a real browser from Lettuce feature files using Selenium. Read
[Lettuce](/book/python/lettuce.html) first if you have not used it yet.

Lettuce is a fairly old project with little recent maintenance. The code here uses Selenium 4 and
has not been run against the latest Lettuce release. If you are starting a new project, consider
a more actively maintained BDD tool.

A complete example project is in the
[Lettuce Selenium repo on GitHub](https://github.com/testcookbook/python-lettuce-selenium).

## Install

```
$ pip install lettuce selenium
```

Selenium 4 finds a matching ChromeDriver for you, so you only need Chrome installed.

## Project layout

```
lettuce-selenium/
├── features/
│   ├── example.feature
│   └── steps.py
```

## The feature

`features/example.feature`:

```gherkin
Feature: Example domain

  Scenario: The home page shows the expected heading
    Given I open "https://example.com"
    Then I should see the heading "Example Domain"
```

## The steps

`features/steps.py`:

```python
from lettuce import before, after, step, world
from selenium import webdriver
from selenium.webdriver.common.by import By


@before.all
def set_up_browser():
    world.browser = webdriver.Chrome()


@after.all
def tear_down_browser(total):
    world.browser.quit()


@step(r'I open "(.*)"')
def open_url(step, url):
    world.browser.get(url)


@step(r'I should see the heading "(.*)"')
def check_heading(step, text):
    heading = world.browser.find_element(By.TAG_NAME, "h1")
    assert heading.text == text, "expected %r, got %r" % (text, heading.text)
```

`@before.all` starts one browser for the whole run, and `world` shares it between steps.
`@after.all` closes it when the run finishes.

## Run it

From the project root:

```
$ lettuce
```

Lettuce prints each step as it runs and reports how many passed or failed.
