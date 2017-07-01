---
layout: default
---
# Robot Framework

Robot Framework is a Test driven development framework.  You can utilize it by a keyword driven approach or a more BDD approach using a Gherkin style test.

## Getting started.

First off we need to setup a little environment stuff.  Hopefully starting out you have some basic Python skills.  Lets install Robot Framework.

```
$ pip install robotframework
```

## Your First Test.
Once it is installed we can now start examining how we can create some tests. Lets assume we want to test adding up a couple of numbers.  For the first test we will focus on a keyword driven development.

***keyword.robot***
```robot
*** Settings ***
Documentation     Example Keyword Test

Library    AdderLibrary.py

*** Test Cases ***
Addition
    Add input    3    5
    Total    8
```

You will notices from the keyword.robot file that there are 2 main headings, surrounded by three asterisks. The first section covers what the settings needed are and the other is a section for test cases.

Within the Settings we want to document what the tests are about, and we also need to include a library. This library will be a Python script that will run to automate the specific tests.

The last section is the Test Cases.  Here you can have a descriptive test case. In this case it says Addition.  Followed by 2 keyword lines. Add input and Total.

> if you are rather new to Python keep in mind that spacing is very important. It is also important in the robot files as well.  While you are looking at the code presented, the large spaced areas are 4 spaces wide.

## Define your tests.

Once you have test file to describe what you are doing. Then its time to write code to actually test what was described.  Create a file "AdderLibrary.py". You might remember it from the settings of the robot file we created.

***AdderLibrary.py***

```python
class AdderLibrary(object):
    """
    Tests for AdderLibrary
    """

    def __init__(self):
        self._result=0

    def add_input(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def total(self, expected):
        self._result = self.a + self.b
        if self._result != int(expected):
            raise AssertionError('%s != %s' % (self._result, expected))
```

For this example we will test within just this file to demonstrate how keywords work.  Normally the actual functionality would be in its own class file.

Take a look at the add_input definition.  When you used the keyword "Add input" in the robot file it will be translated to "add_test".  The first word will be capitalized and the underscore will become a space.  After add_test we
also have 3 arguments. Self, a and b which will be the numbers that we want to add.

Finally take a look at the total function.  This does 2 distinct things.  First it adds up the 2 numbers and returns the value to "self.\_result". Secondly we have an if block. This does a simple comparison to validate if the expected value matches that which we added up.  If it is equal we are fine.  However if things are not equal then we need to assert an error followed by some message that describes what the issue is.

***Terminal***
```
$ robot keyword.robot
==============================================================================
Keyword :: Example Keyword Test                                               
==============================================================================
Addition                                                              | PASS |
------------------------------------------------------------------------------
Keyword :: Example Keyword Test                                       | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  /home/user/robotframework/output.xml
Log:     /home/user/robotframework/log.html
Report:  /home/user/robotframework/report.html
```

## Gherkin

You have completed your first test using keywords.  But what if we wanted to write using a style similar to a Gherkin format?  Well your in luck.  Lets create a file called "gherkin.robot".

***gherkin.robot***
```
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
```

Within this file you will see a new header called Keywords, and the Test Cases will look like Given, When and Then.  The new section Keywords is a little different than you might expect from something like Cucumber.  With Robot Framework your step definition translation is happening within the test file not the step definition.

Take note from the Given we want to get 2 different numbers and add them.  On the parts that we want to get numbers from we have this "${a}" and "${b}".  The dollar sign and the brackets tells the framework that these particular arguments could change and we might want to reuse that functionality later.  

Once the step definition is described we can then add keyword functions just like we did on the keyword.robot file.

***Terminal***
```
$ robot gherkin.robot
==============================================================================
Gherkin :: Example Gherkin Style Test                                         
==============================================================================
Addition                                                              | PASS |
------------------------------------------------------------------------------
Gherkin :: Example Gherkin Style Test                                 | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  /home/user/robotframework/output.xml
Log:     /home/user/robotframework/log.html
Report:  /home/user/robotframework/report.html
```
