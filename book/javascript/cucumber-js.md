---
layout: default
---
# CucumberJS Introduction

In a console window initialize a simple npm project.

```
mkdir -p firstTest
cd firstTest
mkdir features
mkdir -p features/step_definitions
mkdir -p features/support
npm init -f
```

Install cucumber and assert packages and save to package file

```
cd firstTest
npm install cucumber assert --save-dev
```

Install cucumber and assert packages and save to package file

Create your first feature file written in [Gherkin](/book/common-automation-concepts/gherkin.html).

```Gherkin
Feature: First Test
    Scenario: Adding Numbers
        Given numbers 2 and 5
        When they are added together
        Then the total should be 7
```

Build your first step definitions.

```javascript
var assert = require('assert');
module.exports = function () {
    var a, b, t;
    this.Given(/^numbers (\d+) and (\d+)$/, function (arg1, arg2) {
        a = Number(arg1);
        b = Number(arg2);
    });

    this.When(/^they are added together$/, function () {
        t = a + b;
    });

    this.Then(/^the total should be (\d+)$/, function (arg1) {
        assert.equal(t, 7);
    });
}
```
