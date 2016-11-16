---
layout: default
title:  "Frisby.js"
description: "Testing REST services with Frisby.js"
---
# Testing REST services with Frisby.js

Frisby is a testing framework for testing a REST api. It has built in matchers
and Jasmine built into its core.  This allows you to have a clean and concise
way to implement and run your tests.

## Getting Started.

As with any framework or testing tool that you may use a little setup is
required.  If you haven't already install NodeJS on your system.  Once that is
installed you can create a basic npm project and install some packages.  If you
have never initialized a npm project. Check out the chapter on [Initializing a
NodeJS project.](/book/programming/javascript/npm_project.html)

Now you should have a package.json in your test directory similar to the one
above.  Chances are you already have some sort of package json that you could
install packages too.  If so you can skip the init part and start installing
required packages.


<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>


```
$ npm install --save-dev frisby jasmine-node
$ mkdir specs
```



<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
  On the Frisby.js webpage it says to install jasmine-node like.
  "npm install -g jasmine-node" The -g means global.  This would allow you to
  run jasmine-node from anywhere.  I prefer to put it in the save-dev so that
  all of the packages are contained within the node_modules folder within the
  project.
</div>

Since we installed jasmine-node using the --save-dev flag we should update the
test task on the package json.  This will allow for a clean way to run the tests.

<header class="cm1 w3-blue">
  {% include fileIcon.html%}
  steps.py
</header>

```json
{
  "name": "test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "./node_modules/.bin/jasmine-node specs"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "frisby": "^0.8.5",
    "jasmine-node": "^1.14.5"
  }
}
```

You can now run your specs using npm test.

<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

```
$ npm test
> test@1.0.0 test /home/ben/exp/test
> jasmine-node specs

Finished in 0.001 seconds
0 tests, 0 assertions, 0 failures, 0 skipped
```

Once you have a basic running test suite its time to write our first spec.  

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
  All spec files must end in "spec.js" like "test_spec.js" or "yourTestspec.js"
</div>

## Your first spec

<header class="cm1 w3-blue">
  {% include fileIcon.html%}
  first_spec.js
</header>

```javascript
var frisby = require('frisby');
frisby.create('Get Brightbit Twitter feed')
  .get('http://www.testcookbook.com/lib/REST/test.json')
  .expectStatus(200)
.toss();
```

Now try running your tests with "npm test"

<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

```
$ npm test

> test@1.0.0 test /home/ben/exp/test
> jasmine-node specs

.

Finished in 0.452 seconds
1 test, 1 assertion, 0 failures, 0 skipped
```
