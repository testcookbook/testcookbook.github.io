---
layout: default
title:  "Gradle"
description: "Create a Gradle project"
date:   2016-11-08 08:52:00 -0500
---
# Create a Gradle JVM Project

Gradle is a build tool that allows package dependency resolutions as well as
tasks to complete and test your application.

When getting started it is recommended that you download the latest version of
gradle from [https://gradle.org/](https://gradle.org/).  You will also need
Java on your system too.  You can get the jdk from Oracle.  Once you have
installed Java and downloaded Gradle you can update your paths and init a project.

<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

```
$ export PATH=$PATH:/path/to/gradle/bin
$ mkdir YourProject
$ gradle init --type=java-library
```

Gradle will now build a basic project structure for Java.  If you look in the
directory you will have a src directory.  This is where you can put your
application source files and tests.

To run the tests


<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>


```
$ gradle test
```
