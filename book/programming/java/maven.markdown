---
layout: default
title:  "Maven"
description: "Create a Maven project?"
date:   2016-11-08 08:52:00 -0500
---
# Create a Maven Project

Maven is a build tool for the Java ecosystem.  It provides package management
along with tasks to help you with the build process.  If you are starting out
a new project you can initialize your project with a few steps.

You will need to install a couple of dependencies first.  You will need the Java
JDK from Oracle, and Maven.  You can download Maven and get more documentation
about it from [https://maven.apache.org/](https://maven.apache.org/).  Once they
are installed you also need to make sure that your PATH is updated appropriately.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ export PATH=$PATH:/path/to/jdk/bin:/path/to/maven/bin
$ mvn archetype:generate
    -DgroupId=project
    -DartifactId=project
    -DarchetypeArtifactId=maven-archetype-quickstart
{% endhighlight %}
</div>
</div>

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
On a small note you may see documentation that says to use
'mvn archetype:create'.  As of Maven v3 that has depreciated and you should use
'mvn archetype:generate'.
</div>


This will create a basic directory structure for your new project and a few
sample files. There will be a pom.xml, app source and an app test file.  

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
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
                {% endhighlight %}
</div>
</div>

To run your first tests run 'mvn test'.
