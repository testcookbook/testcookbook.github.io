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

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
If you chose Maven open up the 'pom.xml' and change to the latest version of
JUnit which at this time is '4.12'.  Older versions of JUnit work a little
different and may not compile as expected for these lessons.
</div>

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ export PATH=$PATH:/path/to/gradle/bin
$ mkdir YourProject
$ gradle init --type=java-library
{% endhighlight %}
</div>
</div>

Gradle will now build a basic project structure for Java.  If you look in the
directory you will have a src directory.  This is where you can put your
application source files and tests.

To run the tests

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ gradle test
{% endhighlight %}
</div>
</div>
