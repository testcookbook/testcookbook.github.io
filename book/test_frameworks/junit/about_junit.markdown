---
layout: default
title:  "JUnit"
---
# JUnit

JUnit is a Java framework for writing repeatable tests.  Primarily these would
be unit tests, however you can bend it to your particular needs.

## Getting Started

When working with most Java projects and Maven you generally have a standard
directory structure like.

{% highlight text %}
.
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── AddNumber.java
    └── test
        └── java
            └── AddNumberTest.java
{% endhighlight %}

Under src you will see main and test.  Main will store you application or
classes.  Test will store your tests for those classes.  The easiest way to get
dependencies is to add some info to a "pom.xml" file for Maven.  For this
example the dependency that we care about it junit.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  pom.xml
</header>

<div class="w3-container">
{% highlight xml %}
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>junit-test-example</groupId>
  <artifactId>junit-test-example</artifactId>
  <packaging>jar</packaging>
  <version>1.0</version>
  <name>junit-test-example</name>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.12</version>
      <scope>test</scope>
    </dependency>
 </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.5.1</version>
        <configuration>
          <source>1.6</source>
          <target>1.6</target>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
{% endhighlight %}
</div>
</div>

Once you have prepared your Maven configuration you can start writing a basic
unit test that can validate adding 2 numbers.

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
$ mvn test
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

If you were to run "mvn test" now you would get an error since AddNumber has
not been created.  Lets see if we can make this test pass with some code.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  src/main/java/AddNumber.java
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

Now try running "mvn test".  You should get something like.

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
