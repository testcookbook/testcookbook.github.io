---
layout: default
---
# All about Lettuce

Lettuce is a Python BDD type clone of Cucumber.  To the day Lettuce does not have quite all the features of Cucumber but it can still do a great job describing and performing BDD on your application.

## Install
The easiest way to get started is to install Lettuce using pip. If you are new to Python, you might want to spend a little time understanding pip and basic Python techniques.

```
$ pip install lettuce
```

> You might have to install python-Levenshtein depending on your Python install.

```
$ pip install python-Levenshtein
```
Now lets create some basic folder structure.

```
$ mkdir lettuce
$ cd lettuce
$ mkdir features
```

Lets create a feature file using [Gherkin](/book/common-automation-concepts/gherkin.html) within the features folder.

***test1.feature***
```gherkin
Feature: Test 1

  Scenario: Add 2 Numbers
    Given There are numbers 2 and 3
    When added together
    Then they equal 5
```

Once we have the feature lets build us some easy steps to make them pass.

> If you are new to Python please take care to note the indentions in your .py files.  General rule of thumb on Python is to use 4 spaces.

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
