# Frisby.js, Test the REST

Frisby is a testing framework for testing a REST api. It has built in matchers and Jasmine built into its core.  This allows you to have a clean and concise way to implement and run your tests.

## Getting Started.

As with any framework or testing tool that you may use a little setup is required.  If you haven't already install NodeJS on your system.  Once that is installed you can create a basic npm project and install some packages.

```
$ npm install --save-dev frisby jasmine-node
$ mkdir specs
```
> On the Frisby.js webpage it says to install jasmine-node like. "npm install -g jasmine-node" The -g means global.  This would allow you to run jasmine-node from anywhere.  I prefer to put it in the save-dev so that all of the packages are contained within the node_modules folder within the project.


Since we installed jasmine-node using the --save-dev flag we should update the test task on the package json.  This will allow for a clean way to run the tests.

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

```
$ npm test
> test@1.0.0 test /home/ben/exp/test
> jasmine-node specs

Finished in 0.001 seconds
0 tests, 0 assertions, 0 failures, 0 skipped
```

Once you have a basic running test suite its time to write our first spec.  

> All spec files must end in "spec.js" like "test_spec.js" or "yourTestspec.js"

## Your first spec

```javascript
var frisby = require('frisby');
frisby.create('Get Brightbit Twitter feed')
  .get('http://www.testcookbook.com/lib/REST/test.json')
  .expectStatus(200)
.toss();
```

Now try running your tests with "npm test"

```
$ npm test

> test@1.0.0 test /home/ben/exp/test
> jasmine-node specs

.

Finished in 0.452 seconds
1 test, 1 assertion, 0 failures, 0 skipped
```
