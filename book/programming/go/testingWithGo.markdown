---
layout: default
title:  "Testing with Go"
description: "Testing with Go"
---
# Testing with Go

Go provides a testing package that is intended to be used with the command
"go test".  To get started create a file like "string&#95;test.go". Notice the
file name contains "&#95;test.go".  This is key for Go to find the test files
that you are using.

Once you create the file you can create a test like the file below.

```go
package stringtest
import "testing"

func TestValue(t *testing.T) {
  var v string
  v = "Hi"
  if v != "Hello" {
    t.Error("Expected Hello but got", v)
  }
}
```

What is going on here?  To start we tell Go what package we are working with and
import the testing package.  From there we can create a test function.  For this
example we are going to test a value for a specific string.

In other test environments there are built in matchers that you would use.  In
Go are able to define what that criteria is and throw an error when appropriate.
For this string value we want to check if the string v is equal to "Hello". If
it is not, throw an error with a message describing what the issue is.

To run your tests.

```text
$ go test
```
