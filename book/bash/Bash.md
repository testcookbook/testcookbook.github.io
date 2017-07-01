---
layout: default
---
# Bash

Bash or Bourne-again shell is a POSIX compliant shell commonly used on Unix and Linux environments.  Bash can also be installed with Git or Cygwin, etc on Windows.

Scripting in Bash can be a powerful tool in your arsenal for testing.  You can use it to run a certain set of commands to deploy some code, or create an environment.  You can also use it as a testing framework and assert the validity of things running.

### Basics

#### ECHO

```bash
echo "Hello World"
```

The "echo" statement allows you to write text to the screen.

---

#### IF

```bash
if [ true ]; then
  echo "True"
fi
```

If statements allow you to have some checks and balances in you code to do different things.  HINT: if you are having issues with the if statement make sure you have the spaces before and after the \[\] brackets

---

#### FUNCTIONS

```bash
test()
{
    echo "TESTING"
}
```

This is a simple function.  You can use it within your script and it will write "TESTING" to the screen.

---

### Putting Them Together

Lets put these basic steps for Bash together and make an assert\_equal function.  Normally an assert function will take 2 arguments and return true if they are equal and false if they are not. Lets start with a basic declaration of the assert function and some code of how we are going to use it.

```bash
assert_equal ()
{

}

assert_equal "Truth" "Truth"
```

Now that we have a basic framework you can see that we are sending 2 strings of text to the assert\_equal function.  In verifying that we have the proper amount of arguments lets use an if to verify that we have both strings.

```bash
assert_equal ()
{
    if [ -z $2 ]; then
        echo "Missing Arguments: assert_equal arg1 arg2"
        return 99
    fi
}

assert_equal "Truth" "Truth"
```

There are some new techniques here.  Starting with the if statement.  There is a -z $2 within the brackets.  $2 is how you reference argument 2 from the function call.  When we actually return a proper true false we will use $1 and $2.  The -z is very different from what you would see in other languages.  The -z tells us that the length of the string is zero.  If there is no argument 1 or argument 2 listed after the assert\_equal then it will be true and run the code within the if.

The other item that is not like the others is the return statement.  The return statement allow us to send an exit code that can mean specific things to a user.  Normally when an application works like it is suppose to you would return a 0.  However in this case, missing an argument is an error and we want to know that our test is failing due to our scripting as soon as possible.  If there are no arguments here we return back a 99.  You can really put almost any number from 0 to 255.  Anything over 0 however signals the OS that something failed.

We are off to a good start to an assert\_equal function.  Now we need to deliver a true or false back.

```bash
assert_equal ()
{
    if [ -z $2 ]; then
        echo "Missing Arguments: assert_equal arg1 arg2"
        return 99
    fi
    [ $1 == $2 ]
}

assert_equal "Truth" "Truth"
```

Lastly we fish with the last line of the function returning a conditional that will return either true or false.

