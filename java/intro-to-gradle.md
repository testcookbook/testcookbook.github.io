# Create a Gradle JVM Project {#create-a-gradle-jvm-project}

Gradle is a build tool that allows package dependency resolutions as well as tasks to complete and test your application.

When getting started it is recommended that you download the latest version of gradle from [https://gradle.org/](https://gradle.org/). You will also need Java on your system too. You can get the jdk from Oracle. Once you have installed Java and downloaded Gradle you can update your paths and init a project.

Command Line

```
$ export PATH=$PATH:/path/to/gradle/bin
$ mkdir YourProject
$ gradle init --type=java-library

```

Gradle will now build a basic project structure for Java. If you look in the directory you will have a src directory. This is where you can put your application source files and tests.

To run the tests

Command Line

```
$ gradle test
```



