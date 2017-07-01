---
layout: default
---
# CucumberJS and Chai Assertions Three Ways

**Ingredients**

* NodeJS
* Cucumber
* Chai


**Bake Time**

* 10 - 15 min

**Instructions**

In a console window initialize a simple npm project.

```bash
mkdir -p firstTest
cd firstTest
mkdir features
mkdir -p features/step_definitions
mkdir -p features/support
npm init -f
```

Install cucumber and assert packages and save to package file

```bash
cd firstTest
npm install cucumber chai --save-dev
ls
```

Create your first feature file.

```Gherkin
Feature: First Test
    Scenario: Adding Numbers
        Given numbers 2 and 5
        When they are added together
        Then the total should be 7
```

Build your first step definitions.

```javascript
var chai = require('chai');
var assert = chai.assert;
var expect = chai.expect;
var should = chai.should();

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
        expect(t).to.equal(7);
        t.should.equal(7);
    });
}
```
