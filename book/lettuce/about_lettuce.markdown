---
layout: default
title:  "All about Lettuce"
description: "Intro to the Python Lettuce framework for testing."
---
# All about Lettuce

Lettuce is a Python BDD type clone of Cucumber.  To the day Lettuce does not
have quite all the features of Cucumber but it can still do a great job
describing and performing BDD on your application.

## Install
The easiest way to get started is to install Lettuce using pip.  If you are new
to Python, you might want to spend a little time understanding pip and basic
Python techniques.

<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

```
$ pip install lettuce
```

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%} You might have to install python-Levenshtein depending
on your Python install.
</div>

```
$ pip install python-Levenshtein
```
Now lets create some basic folder structure.

<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

```
$ mkdir lettuce
$ cd lettuce
$ mkdir features
```

Lets create a feature file using [Gherkin](/book/programming/gherkin.html) within the features folder.

<header class="cm1 w3-blue">
  {% include fileIcon.html%}
  test1.feature
</header>

```gherkin
Feature: Test 1

  Scenario: Add 2 Numbers
    Given There are numbers 2 and 3
    When added together
    Then they equal 5
```

Once we have the feature lets build us some easy steps to make them pass.

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
  If you are new to Python please take care to note the indentions in your
  .py files.  General rule of thumb on Python is to use 4 spaces.
</div>

<header class="cm1 w3-blue">
  {% include fileIcon.html%}
  steps.py
</header>

```python
from lettuce import *
@step(u'Given There are numbers 2 and 3')
def given_there_are_numbers_2_and_3(step):
    world.a = 2
    world.b = 3

@step(u'When added together')
def when_added_together(step):
    world.total = world.a + world.b

@step(u'Then they equal 5')
def then_they_equal_5(step):
    assert (world.total == 5), 'Amount should equal 5'
```
