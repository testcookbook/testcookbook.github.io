---
layout: default
---
# JUnit 5 {#junit}

JUnit is a Java framework for writing repeatable tests. Primarily these would be unit tests, however you can bend it to your particular needs.

## Getting Started {#getting-started}

When working with most Java projects you generally want to use a build tool. For JUnit tests there are a couple of build tools that you are most likely to see and use. For this exercise feel free to try out either Maven or Gradle. If this is your first Java project check out the section on initializing [Maven](https://www.testcookbook.com/book/programming/java/maven.html) or [Gradle](https://www.testcookbook.com/book/programming/java/gradle.html).  You can view a working [pom.xml](https://github.com/testcookbook/junit5/blob/master/pom.xml)

Once you have created a new Java project, create a new file within the ‘src/test/java/path/to/app’ directory called ‘Math.java’.

src/test/java/path/to/app/Math.java

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class MathTest {
  
  @Test
  public void addingNumbers() {
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

Now that we have a real basic test lets try a small amount of TDD and build a class that adds up 2 numbers. Making some modifications to the MathTest.java so that it looks like.

MathTest.java

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class MathTest {
  
  @Test
  public void addingNumbers() {
    Math m = new Math();
    assertEquals(m.Add(2, 3), 5);
  }

}
```

If you were to run the tests now you would get an error since Math has not been created. Lets see if we can make this test pass with some code.

src/main/java/path/to/app/Math.java

```java
public class Math {

  public int Add(int a, int b) {
    return a + b;
  }

}
```

Now try running the tests. You should get something like.

Command Line

```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running MathTest
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.008 s - in MathTest
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 4.041 s
[INFO] Finished at: 2018-05-07T15:06:27-05:00
[INFO] Final Memory: 17M/221M
[INFO] ------------------------------------------------------------------------
```

![Travis Build Icon](https://travis-ci.org/testcookbook/junit5.svg?branch=master)

All of the source of this lesson is on [Github](https://github.com/testcookbook/junit5).

