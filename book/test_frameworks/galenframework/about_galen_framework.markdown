---
layout: default
title:  "Galen Framework"
---
# Galen Framework

Galen Framework is a tool primarily based to test the user interface for a
website.  In the world of thing like mobile first and responsive design. It can
be quite a task to validate what an application looks like on many different
devices and browsers. Galen works to solve this problem by providing a different
test and spec format geared towards this goal.

There are 3 main types of files within a Galen Framework project.  Test, GSpec,
and Javascript.  Each of these can be used to define actions and work flow and
tested through Selenium to the browser of choice.

## Install
---
By far the easiest way to install is if you already have npm installed. If not
you can goto the Galen Framework website and download the tool.
<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ sudo npm install -g galenframework-cli
{% endhighlight %}
</div>
</div>

## Config
---
Galen has a central config file called "galen.config".  With it you can specify
many of the workings for Galen.  For now lets just set the default browser to
Chrome.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  galen.config
</header>

<div class="w3-container">
{% highlight language %}
galen.default.browser=chrome
{% endhighlight %}
</div>
</div>

## Your first spec
---
To start out we will make a spec that looks at the Galen Test page and validates
the header height and the content width and height.  To do so we first need to
make @objects.  These will be html elements that have specific id or class etc.

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
Spacing is somewhat important with Galen however your spacing can be from 1 to 8
space long.  Not Tabs.  I decided to stick with 4 spaces.  Once the objects are
created then you must create a section for the tests delimited by the = sign on
both sides of the text.  Then lastly we can define what we would like to look
for on each object to validate.
</div>

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  home-page.gspec
</header>

<div class="w3-container">
{% highlight galen %}
@objects
    header   id    header
    content  id    content

= Main Section =
    header:
        height    100px
    content:
        height    220px
        width     325px

{% endhighlight %}
</div>
</div>

To run just this spec we can type the following in the command line.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
$ galen check home-page.gspec \
  --url http://samples.galenframework.com/tutorial1/tutorial1.html \
  --size 640x480 --htmlreport ./report

========================================
Test: home-page.gspec
========================================
Starting ChromeDriver 2.24.417424 (c5c5ea873213ee72e3d0929b47482681555340c3) on port 13342
Only local connections are allowed.
check  home-page.gspec --url http://samples.galenframework.com/tutorial1/tutorial1.html --size 640x480 --htmlreport ./report -Dwebdriver.chrome.driver=/pathto/chromedriver
= Main Section =
    header:
        height    100px

    content:
        height    220px
        width     325px


========================================
----------------------------------------
========================================
Suite status: PASS
Total tests: 1
Total failed tests: 0
Total failures: 0

{% endhighlight %}
</div>
</div>

Now that we have a spec lets see if we can build a test around it along with
setting up some variables for different browser sizes.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  home-page.test
</header>

<div class="w3-container">
{% highlight galen %}
@objects
@@ parameterized
    | deviceName | tags      | size     |
    | Mobile     | mobile    | 320x600  |
    | Tablet     | tablet    | 640x480  |
    | Desktop    | desktop   | 1024x800 |
Home page on ${deviceName} device
    http://samples.galenframework.com/tutorial1/tutorial1.html ${size}
        check home-page.gspec --include "${tags}"
{% endhighlight %}
</div>
</div>

To run the tests we just need to use Galen test.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
$ galen test home-page.test --htmlreport ./report

========================================
Test: Home page on Mobile device
========================================
Starting ChromeDriver 2.24.417424 (c5c5ea873213ee72e3d0929b47482681555340c3) on port 8750
Only local connections are allowed.
check home-page.gspec --include "mobile"
= Main Section =
    header:
        height    100px

    content:
        height    220px
->      width     325px
->      :   "content" width is 329px instead of 325px

========================================
Test: Home page on Tablet device
========================================
Starting ChromeDriver 2.24.417424 (c5c5ea873213ee72e3d0929b47482681555340c3) on port 12196
Only local connections are allowed.
check home-page.gspec --include "tablet"
= Main Section =
    header:
        height    100px

    content:
        height    220px
        width     325px

========================================
Test: Home page on Desktop device
========================================
Starting ChromeDriver 2.24.417424 (c5c5ea873213ee72e3d0929b47482681555340c3) on port 8222
Only local connections are allowed.
check home-page.gspec --include "desktop"
= Main Section =
    header:
        height    100px

    content:
        height    220px
->      width     325px
->      :   "content" width is 724px instead of 325px


========================================
----------------------------------------
========================================
Failed tests:
    Home page on Mobile device
    Home page on Desktop device

Suite status: FAIL
Total tests: 3
Total failed tests: 2
Total failures: 2
There were failures in galen tests

{% endhighlight %}
</div>
</div>

You will probably notice some failures this time.  The width changes with the
different resolutions.  Lets add some tags to the home-page.gspec.  To do this
we will use the @on followed by a tag.  "@on tagname".

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  home-page.gspec
</header>

<div class="w3-container">
{% highlight galen %}
@objects
    header   id    header
    content  id    content

= Main Section =
    header:
        height    100px
    content:
        height    220px
    @on mobile
        content:
            width    329px
    @on tablet
        content:
            width    325px
    @on desktop
        content:
            width    724px


{% endhighlight %}
</div>
</div>

Running once more

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
$ galen test home-page.test --htmlreport ./report
========================================
Test: Home page on Mobile device
========================================
Starting ChromeDriver 2.24.417424 (c5c5ea873213ee72e3d0929b47482681555340c3) on port 26700
Only local connections are allowed.
check home-page.gspec --include "mobile"
= Main Section =
    header:
        height    100px

    content:
        height    220px
        width     329px

========================================
Test: Home page on Tablet device
========================================
Starting ChromeDriver 2.24.417424 (c5c5ea873213ee72e3d0929b47482681555340c3) on port 4679
Only local connections are allowed.
check home-page.gspec --include "tablet"
= Main Section =
    header:
        height    100px

    content:
        height    220px
        width     325px

========================================
Test: Home page on Desktop device
========================================
Starting ChromeDriver 2.24.417424 (c5c5ea873213ee72e3d0929b47482681555340c3) on port 6030
Only local connections are allowed.
check home-page.gspec --include "desktop"
= Main Section =
    header:
        height    100px

    content:
        height    220px
        width     724px


========================================
----------------------------------------
========================================
Suite status: PASS
Total tests: 3
Total failed tests: 0
Total failures: 0

{% endhighlight %}
</div>
</div>


Thats the very a very basic way to get started with Galen Framework.  There is
more documentation on their website.
[http://www.galenframework.com](http://www.galenframework.com)
