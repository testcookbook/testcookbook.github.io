---
layout: default
---
# Create a Maven Project {#create-a-maven-project}

Maven is a build tool for the Java ecosystem. It provides package management along with tasks to help you with the build process. If you are starting out a new project you can initialize your project with a few steps.

You will need to install a couple of dependencies first. You will need the Java JDK from Oracle, and Maven. You can download Maven and get more documentation about it from[https://maven.apache.org/](https://maven.apache.org/). Once they are installed you also need to make sure that your PATH is updated appropriately.

Command Line

```
$ export PATH=$PATH:/path/to/jdk/bin:/path/to/maven/bin
$ mvn archetype:generate
    -DgroupId=project
    -DartifactId=project
    -DarchetypeArtifactId=maven-archetype-quickstart

```

> On a small note you may see documentation that says to use 'mvn archetype:create'. As of Maven v3 that has depreciated and you should use 'mvn archetype:generate'.

This will create a basic directory structure for your new project and a few sample files. There will be a pom.xml, app source and an app test file.

Command Line

```
$ tree
.
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── project
    │           └── App.java
    └── test
        └── java
            └── project
                └── AppTest.java

```

To run your first tests run ‘mvn test’.

