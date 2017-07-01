---
layout: default
---
# Assumption Styles

Automation testing is really all about defining what your application is supposed to do and making sure it continues to do so.  In almost every programming framework you generally get one of three different assumption styles.  Assert, Expect, Should.

Note: Some frameworks will let you use any combination of these.

In the end, the three of these styles do the same thing they assume that some element or value will have a quantified relationship with an answer that you require.  The reason there are a few ways to describe is about readability and preference.

Let's take a look at some pseudo code for each.

```
let someValue = true

expect(someValue).toBeTrue()

assert(someValue).isTrue()

someValue.should.beTrue()
```

Notice that in each case we have a variable "someValue", and in each case, we want to determine whether it is true.  Each assumption style reads just like a sentence.  Expect "someValue" to be true.  Assert "someValue" is true.  "someValue" should be true.

### Behind the scenes.

The more important part to note about each of these styles is really what is happening during the testing.  Each one of these styles is required to accept some value and make sure that it is correct.  When an error happens we want to create a failure in the test build.  In most cases, this will generate an exit code of the test suite greater than 0.  

### Build your own expect or assertion.

```
class expect
    
    var expectedValue

    expect(val)
        expectedValue = val
    end
    
    toBeTrue()
        if expectedValue == true
            return true
        else
            throw error("expected #{expectedValue} to have been true")
        end
    end
end
```

This is a quick a dirty basic implementation of an expect statement.  Assert works the same way you can replace the text for expect with assert.  

### Building your own should.

Should is generally a little different that expect and assert.  It is usually added as a child or prototype to another object or class.  For example lets say you have a Boolean.

```
class should
    beTrue()
        if expectedValue == true
            return true
        else
            throw error("expected #{expectedValue} to have been true")    
        end
    end
end

Boolean.prototype.should = should

Boolean test = true

test.should.beTrue();
```

There are some potential cons to using should.  As you notice you are adding foreign code to your specific object. Depending on how much you really want to use this format keep in mind it won't be quite as pure as the expect and assert styles.