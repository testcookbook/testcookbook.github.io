---
layout: default
title:  "Wait VS Sleep"
description: "Wait VS Sleep"
date:   2016-09-29 06:22:12 -0500
categories: [wait, sleep]
---
# Wait VS Sleep

Chances are you work for a big company and you are testing many things but you
have some instances which are either flaky or you need to just pause for a bit.
With automation, especially on browser applications pausing is a good thing to
understand.  In general there are 2 kinds of pausing that work.  Wait and Sleep.

## Sleep

The sleep statement has been around for quite a long time in the world of
software development.  As a tester sometimes it seems like the easiest way to
delay whatever is going on so that the rest of your test may pass.  

{% highlight javascript %}
$('#someElement').click();
browser.sleep(3000);
$('#someOtherElement').click();
{% endhighlight %}

You might have something that looks similar to the code above.  You try to click
on an element, sleep for 3 seconds and then try to click on another element. The
pros of this is that you have control over how long you wanna delay as long as
you are in front of the code that has that specific value.  But what are the
cons. One issue is you do not know if you might can delay 2 seconds instead of 3.
Why would you care?  Well if you always put a 3 second delay on tests and you
happen to have 100 tests you added 5 minutes or 300 seconds of delay time.  If
at some point they could be 1 second less you could save up to 100 seconds. The
other side to this coin is that maybe if you run your browser tests against a
remote selenium grid you might need a delay of longer than 3 seconds.  

It would sure be nice to have a way that would automatically continue if the
element was present.  In most automation frameworks there exists some form of
a waitForPresence.  If there isn't one they are generally not to complicated to
make your own.  

{% highlight javascript %}
$('#someElement').click();
$('#someOtherElement').waitForPresence();
$('#someOtherElement').click();
{% endhighlight %}

In this example instead of sleeping for 3 seconds, we wait for the element to
be present.  This can be really cool.  For example a pro for this type of delay
is that whether it takes 1 seconds or a few seconds the test can finish in its
most opportune time.  However there is a potential con to waits.  That is the
max time.  Most selenium tools have a max wait time from 10 to 30 seconds.  In
the case of failures at the wait statement each test can take up to that max
time.  Just think if you had 100 tests all with wait failures.  If max time is
30 seconds and 100 tests thats 3000 seconds or 50 minutes.  That is not fun.
At least you know if your tests are taking way to long all of a sudden you
either have a big issue with you code or you have quite a bit of refactoring to
do on your tests.
