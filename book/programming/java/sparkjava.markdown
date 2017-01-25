---
layout: default
title:  "Simple RestApi using Spark"
description: "Create a simple REST api for mocking data using Spark"
date:   2017-01-25 08:52:00 -0500
---
# Create a simple REST api using Spark

Depending on the test environments you have sometimes you may want to build your
own REST api that can mock data for your test scenarios.

## Getting started

Create a new project directory and add Spark dependencies.

```text
mkdir restapi
cd restapi
gradle init --type=java-library
```

Then update your build.gradle file.

```groovy
apply plugin: 'java'
apply plugin: 'application'
mainClassName = "RestApi"

repositories {
    jcenter()
}

dependencies {
    compile 'com.sparkjava:spark-core:2.5.4'
    testCompile 'junit:junit:4.12'
}
```

Create a new file called RestApi.java and place it under the
"restapi/src/main/java" directory.

```java
import static spark.Spark.*;

public class RestApi {
    public static void main(String[] args) {
        get("/", (req, res) -> "Root Route");
        get("/hello", (req, res) -> "Hello World");
    }
}
```
