# JUnit {#junit}

JUnit is a Java framework for writing repeatable tests. Primarily these would be unit tests, however you can bend it to your particular needs.

## Getting Started {#getting-started}

When working with most Java projects you generally want to use a build tool. For JUnit tests there are a couple of build tools that you are most likely to see and use. For this exercise feel free to try out either Maven or Gradle. If this is your first Java project check out the section on initializing[Maven](http://www.testcookbook.com/book/programming/java/maven.html)or[Gradle](http://www.testcookbook.com/book/programming/java/gradle.html).

Once you have created a new Java project, create a new file within the ‘src/main/java/path/to/app’ directory called ‘AddNumberTest.java’.

src/main/java/path/to/app/AddNumberTest.java

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AddNumberTest {
  @Test
  public void addsNumbersExpression() {
    assertEquals(2+3, 5);
  }

}
```

You should now be ready to run your tests.

Command Line

```
# Maven User
$ mvn test

# Gradle User
$ gradle test

```

Now that we have a real basic test lets try a small amount of TDD and build a class that adds up 2 numbers. Making some modifications to the AddNumberTest.java so that it looks like.

AddNumberTest.java

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class AddNumberTest {
  @Test
  public void addsNumbersExpression() {
    AddNumber an = new AddNumber(2, 3);
    assertEquals(an.total, 5);
  }

}
```

If you were to run the tests now you would get an error since AddNumber has not been created. Lets see if we can make this test pass with some code.

src/main/java/path/to/app/AddNumber.java

```java
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
```

Now try running the tests. You should get something like.

Command Line

```
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
```



