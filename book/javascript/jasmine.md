---
layout: default
---
# Jasmine

Jasmine is a BDD or Behavior Driven Development tool for Javascript that is full
service and can be run alone without any extra dependencies.  That means it
contains a runner and expectation libraries. Though it is primarily used for
testing Javascript you can also mix it up with Selenium and other drivers to
test applications and services.

---

## Describe It
Jasmine uses a describe and it format to define the tests.

```javascript
describe("What are the tests about", function() {
  it("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
```

---
## Expectations
For any test tool in order to provide value we must assert or expect that some
return value meets a set of requirements.  In Jasmine you would use the expect
statement followed by a matcher.

A matcher is a function that returns a boolean for different types of
comparison. For example.  toBeTruthy() would validate if the expectation is
true or toBeFalsy() would validate if the expectation is false.

```javascript
//Pass
expect(true).toBe(true);
expect(true).toBeTruthy();

//Fail
expect(false).toBe(true);
expect(false).toBeTruthy();
```

## Pending Tests.
---
Sometimes you may want to put a test in a pending state for your own reasons.
There are a couple of ways you can do that.  The first is from the spec or "it"
level.  All you need to do is add a "x" in front of "it".  When you run your
suite all the tests that do not have a "x" will run.

```javascript
describe("What are the tests about", function() {
  xit("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
```

Another option would be to pend the entire suite.  This way none of the specs within the suite would run but any other suite within your project will.  To do this put a "x" before "describe".

```javascript
xdescribe("What are the tests about", function() {
  it("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
```

## Run specific test or suite.
---
To run a specific test you can put a "f" in front of "it".  When you run Jasmine it will run only that test.

```javascript
describe("What are the tests about", function() {
  fit("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
```

The same is true for a suite.  To run just the suite put a "f" in front of describe.

```javascript
fdescribe("What are the tests about", function() {
  it("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
```
