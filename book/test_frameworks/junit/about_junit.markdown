---
layout: default
title:  "JUnit"
description: "How to start building JUnit tests."
---
# JUnit

JUnit is a Java framework for writing repeatable tests.  Primarily these would
be unit tests, however you can bend it to your particular needs.

## Getting Started

When working with most Java projects you generally want to use a build tool.
For JUnit tests there are a couple of build tools that you are most likely to
see and use.  For this exercise feel free to try out either Maven or Gradle.  If
this is your first Java project check out the section on initializing
[Maven](/book/programming/java/maven.html) or
[Gradle](/book/programming/java/gradle.html).



Once you have created a new Java project, create a new file within the
'src/main/java/path/to/app' directory called 'AddNumberTest.java'.
<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  src/main/java/path/to/app/AddNumberTest.java
</header>

<div class="w3-container">
{% highlight java %}
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AddNumberTest {
  @Test
  public void addsNumbersExpression() {
    assertEquals(2+3, 5);
  }

}
{% endhighlight %}
</div>
</div>

You should now be ready to run your tests.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
# Maven User
$ mvn test

# Gradle User
$ gradle test
{% endhighlight %}
</div>
</div>

Now that we have a real basic test lets try a small amount of TDD and build a
class that adds up 2 numbers.  Making some modifications to the
AddNumberTest.java so that it looks like.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  AddNumberTest.java
</header>

<div class="w3-container">
{% highlight java %}
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AddNumberTest {
  @Test
  public void addsNumbersExpression() {
    AddNumber an = new AddNumber(2, 3);
    assertEquals(an.total, 5);
  }

}
{% endhighlight %}
</div>
</div>

If you were to run the tests now you would get an error since AddNumber has
not been created.  Lets see if we can make this test pass with some code.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  src/main/java/path/to/app/AddNumber.java
</header>

<div class="w3-container">
{% highlight java %}
public class AddNumber {

  public int num1;
  public int num2;
  public int total;

  public AddNumber(int n1, int n2) {
    num1 = n1;
    num2 = n2;
    total = n1 + n2;
  }

}

{% endhighlight %}
</div>
</div>

Now try running the tests.  You should get something like.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running AddNumberTest
Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.07 sec - in AddNumberTest

Results :

Tests run: 1, Failures: 0, Errors: 0, Skipped: 0

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 2.637 s
[INFO] Finished at: 2016-10-07T11:41:55-05:00
[INFO] Final Memory: 15M/166M
[INFO] ------------------------------------------------------------------------
{% endhighlight %}
</div>
</div>
