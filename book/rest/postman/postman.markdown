---
layout: default
title:  "Intro to Postman"
description: "Wait VS Sleep"
date:   2016-11-08 06:22:12 -0500
categories: [postman]
---
# Intro to Postman

Postman is a modern REST api tool. As with most tools and REST clients you can
give it a url and a set of parameters and receive data from an API.  However
Postman also has another thing up its sleeve.  It has the ability to build test
scripts, collections of tests and has a runner.  If these are attractive to
your test environment they also off tools for CI integrations as well.

![Postman Logo](/lib/images/ic-postman-logo@2x.png)

Currently there are a couple of ways to get Postman.  One of those ways is using
Chrome extensions.  However at the current time it is probably best to install
Postman from their website as a native app, as Chrome extensions are going away.
[https://www.getpostman.com/](https://www.getpostman.com/)

![Postman basic form](/lib/images/postman/postman-basic-form.png)

Now try out your first REST api call.  In the input field where it says 'Enter
request URL' put in the url 'http://www.testcookbook.com/lib/REST/test.json'.
Then hit 'Send'.

![Postman basic results](/lib/images/postman/postman-basic-results.png)

# Writing your first test

Writing your first test is really simple.  To get started find the Tests link
on right under the input field for the url.

![Postman basic tests](/lib/images/postman/postman-basic-tests.png)

Once you click it you will see a bigger form appear below and also a small
quick snippets reference on the right side.

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
  Scripts in Postman are written in Javascript.
</div>


Tests in Postman work by setting a field within an array to true or false.  The
name of that field is also the description for the test.  
<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
An array will have a format that looks like. tests['some value']
</div>

To start off lets write a simple passing and failing test.

```javascript
tests["Pass"] = true;
tests["Fail"] = false;
```

Now when you click on the send button you should get something that looks like
the image below.

![Postman simple test results](/lib/images/postman/postman-simple-test-results.png)

## Operators

A small segment into a little programming knowledge.  When you actually write
tests later on you will be looking for the result of either a function or some
boolean operator combination to give a result. Some common operators that you
might see that result in a boolean would be.

```
| a == b   | returns true if a is equal to b
| a != b   | returns true if a is NOT equal to b
| a === b  | returns true if a is equal to b and the type is the same
| a < b    | returns true if a is less than b
| a > b    | returns true if a is greater than b
| a <= b   | returns true if a is less or equal to b
| a >= b   | returns true if a is greater or equal to b

```

## Test Response Time

So now you know how to assert a passing and failing test lets write a useful
test.  Lets say that we want to make sure that the response time will be less
than 1 second.

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
Remember that responseTime is actuall measured in milliseconds.  So 1000ms is
equal to 1 sec.
</div>

```javascript
tests["Response time < 1 sec"] = responseTime < 1000;
```

## Test Response Body

Many times it is the specific body of the response that you would like to test.
Postman has a variable call responseBody that is exposed containing the results
for your api call.  By default that responseBody is a
[string](/book/glossary/glossary.html#string).  In order to process it neatly
like an object we need to convert it into a JSON. We can convert the string to
JSON by using the JSON.parse function.

```javascript
var jsonData = JSON.parse(responseBody);
```

Once we have created the JSON data then we can make an test for specific data.

```javascript
tests["Test Name"] = jsonData.name === "John Doe";
```

## Test JSON Schema

JSON schema is an important tool when validating a REST api with rest.  You can
read more about it in the chapter on [JSON Schema](/book/rest/json_schema.html).
In order to test the JSON to a schema we will need to first create a JSON object
like in the last example.  Then we need to make a variable called schema to
build our JSON requirements in.

```javascript
var jsonData = JSON.parse(responseBody);
var schema = {
    "properties": {
        "name": {
            "type": "number"
        }   
    }
};

tests["Valid Schema"] = tv4.validate(jsonData, schema);

// If you want to look at the console log for what errored out.
console.log("Validation failed: ", tv4.error);
```

Once you have built your schema you can validate it using Tiny Validator.  Tiny
Validator is included with Postman and assigned to the variable tv4.  To find
more information and other ways to use Tiny Validator check out
[http://geraintluff.github.io/tv4/](http://geraintluff.github.io/tv4/).

Now if you send this query you should notice that there is a failing test.  If
you would like to see why, from the menu bar click View -> Show Postman Console.

![Postman console error](/lib/images/postman/postman-console-error.png)

From looking at the log you will notice that the message is telling us that it
is expecting a number not a string.  Name should actually be a string in this
case.  So in your schema variable change the type for name to string.

```javascript
var schema = {
    "properties": {
        "name": {
            "type": "string"
        }   
    }
};
```

This time when you send the request everything should pass.  

Want to come up with even more ways to test.  Check out the other snippets that
are on Postman. 
