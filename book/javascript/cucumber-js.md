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

Updating your package.json file to run the tests. Within the scripts section of the package.json update the object test with the following.
```
  "scripts": {
    "test": "./node_modules/.bin/cucumber-js"
  },
```

Once you have saved the package.json file you will now be able to run your tests using.

```
npm test
```

Create your first feature file written in [Gherkin](/book/common-automation-concepts/gherkin.html).

```gherkin
Feature: First Test
    Scenario: Adding Numbers
        Given numbers 2 and 5
        When they are added together
        Then the total should be 7
```

Build your first step definitions.

```javascript
const {Given, Then, When} = require('cucumber');
const assert = require('assert');

let a, b, t;

Given('numbers {int} and {int}', function(int, int2) {
    a = int;
    b = int2;
});

When('they are added together', function() {
    t = a + b;
});

Then('the total should be {int}', function(int) {
    assert.equal(t, 7)
});
```

```
$ npm test

> cucumberjs-sample@1.0.0 test /Users/ben/personal/cucumberjs-sample
> cucumber-js

...

1 scenario (1 passed)
3 steps (3 passed)
0m00.003s
```

![Travis Build Cucumber-Js-Sample](https://travis-ci.org/testcookbook/cucumber-js-sample.svg?branch=master)

If you would like to view this all together check it out on [Github](https://github.com/testcookbook/cucumber-js-sample).
