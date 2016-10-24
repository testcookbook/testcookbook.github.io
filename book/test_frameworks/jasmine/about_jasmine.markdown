---
layout: default
title:  "About Jasmine"
description: "Introduction to Jasmine testing in Javascript"
---
# Jasmine

Jasmine is a BDD or Behavior Driven Development tool for Javascript that is full
service and can be run alone without any extra dependencies.  That means it
contains a runner and expectation libraries. Though it is primarily used for
testing Javascript you can also mix it up with Selenium and other drivers to
test applications and services.

## Describe It
---
Jasmine uses a describe and it format to define the tests.

{% highlight javascript %}
describe("What are the tests about", function() {
  it("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
{% endhighlight %}

## Expectations
---
For any test tool in order to provide value we must assert or expect that some
return value meets a set of requirements.  In Jasmine you would use the expect
statement followed by a matcher.

A matcher is a function that returns a boolean for different types of
comparison. For example.  toBeTruthy() would validate if the expectation is
true or toBeFalsy() would validate if the expectation is false.

{% highlight javascript %}
//Pass
expect(true).toBe(true);
expect(true).toBeTruthy();

//Fail
expect(false).toBe(true);
expect(false).toBeTruthy();
{% endhighlight %}

## Implementation
---
There are various different setups that can be accomplished to run Jasmine
tests.  To see how you can run check out one of the implementation sections of
the book.

[Jasmine inline with HTML](/book/web_testing/javascript/jasmine_inline_html.html)

## Pending Tests.
---
Sometimes you may want to put a test in a pending state for your own reasons.
There are a couple of ways you can do that.  The first is from the spec or "it"
level.  All you need to do is add a "x" in front of "it".  When you run your
suite all the tests that do not have a "x" will run.

{% highlight javascript %}
describe("What are the tests about", function() {
  xit("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
{% endhighlight %}

Another option would be to pend the entire suite.  This way none of the specs
within the suite would run but any other suite within your project will.  To
do this put a "x" before "describe".

{% highlight javascript %}
xdescribe("What are the tests about", function() {
  it("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
{% endhighlight %}

## Run specific test or suite.
---
To run a specific test you can put a "f" in front of "it".  When you run Jasmine
it will run only that test.

{% highlight javascript %}
describe("What are the tests about", function() {
  fit("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
{% endhighlight %}

The same is true for a suite.  To run just the suite put a "f" in front of
describe.

{% highlight javascript %}
fdescribe("What are the tests about", function() {
  it("tells us what the spec and expectation is", function() {
    expect("some function or value").toBe(true);
  });
});
{% endhighlight %}
