---
layout: default
title:  "Gauge Test Framework"
description: "Introduction to the Gauge Test Framework"
---
# Gauge Test Framework

Gauge is a test framework created by ThoughtWorks that is geared so that the
business can understand what is being tested.  Whether you do BDD, or TDD, or
some other combination Gauge offers a beautiful reporting structure for your
tests and a flexible back end for running the tests.

## Getting Started

Hop over to [http://getgauge.io](http://getgauge.io) and download the zip file
that is appropriate for your operating system.  Once you have installed Gauge,
then we can run a couple commands to get us ready to run some tests.  For the
purpose of this lesson we will be using Ruby, however you could also do Java or
CSharp.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ mkdir gaugeTests
$ gauge --init ruby
{% endhighlight %}
</div>
</div>

After running these commands you will have your directory setup to run the some
tests.  To run them you can run 'gauge specs'.  
<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
<figure class="highlight">
<pre><code class="language-text" data-lang="text"><span style="color:#0AA"># Specification Heading
</span><span style="color:#A50">  ## Vowel counts in single word	</span><span style="color:#0A0"> ✔</span><span style="color:#0A0"> ✔</span>
<span style="color:#A50">  ## Vowel counts in multiple word	</span><span style="color:#0A0"> ✔</span><span style="color:#0A0"> ✔</span>

Successfully generated html-report to => /home/user/gauge/reports/html-report
Specifications:	1 executed	1 passed	0 failed	0 skipped
Scenarios:	2 executed	2 passed	0 failed	0 skipped

Total time taken: 924ms
</code></pre></figure>
</div>
</div>

After you run the Gauge specs you should now have a reports/html-report
directory.  Within that folder is an 'index.html'.  Open it up in your favorite
browser.

<img src="/lib/images/gaugeReport.png" alt="Gauge Report Image" class="tc-full-image" />

## Building your own specs

Gauge uses a little different style of format than most other tools.  They use
markdown.  Markdown is a light weight HTML template markup language.  One of the
most common uses of markdown is on GitHub for readme.md files.

Lets create a new spec where we add 2 numbers and validate the sum.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  total.spec
</header>

<div class="w3-container">
{% highlight markdown %}
Add numbers
=====================

We would like to add 2 numbers together using add function and validate
that the output is correct.

Adding numbers
---------------------------

tags: add numbers

* If I add "4" and "5" then the total is "9"
{% endhighlight %}
</div>
</div>

Now lets create some steps to run the spec.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  total.spec
</header>

<div class="w3-container">
{% highlight ruby %}
require 'test/unit'
include Test::Unit::Assertions

def add(a, b)
  return a + b
end

step 'If I add <a> and <b> then the total is <c>' do |a, b, c|
   assert_equal(add(a,b), c)
end
{% endhighlight %}
</div>
</div>

Lets run 'gauge specs'.  Uh Oh! we have an error.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
<figure class="highlight">
<pre><span style="color:#0AA">
<span style="color:#0AA"># Specification Heading</span>
<span style="color:#A50">  ## Vowel counts in single word	</span><span style="color:#0A0"> ✔</span><span style="color:#0A0"> ✔</span>
<span style="color:#A50">  ## Vowel counts in multiple word	</span><span style="color:#0A0"> ✔</span><span style="color:#0A0"> ✔</span>

<span style="color:#0AA"># Add numbers</span>
</span><span style="color:#A50">  ## Adding numbers	</span><span style="color:#A00"> ✘</span><span style="color:#A00">
        Failed Step: If I add "4" and "5" then the total is "9"
        Specification: specs/total.spec:12
        Error Message: <"45"> expected but was
        <"9">.
</span>
Successfully generated html-report to => /home/user/gauge/reports/html-report
Specifications:	2 executed	1 passed	1 failed	0 skipped
Scenarios:	3 executed	2 passed	1 failed	0 skipped

Total time taken: 1.372s
</pre>
</figure>
</div>
</div>

Since we are driving out development as we test.  We need to do a little work to
the add function. Change the add function in the total.rb file to the following.
This will convert the text in the step to an integer so that it can be added.
Then we convert the total back to a string so we can compare the value with the
expectation in the step.

{% highlight ruby %}
def add(a, b)
  return (a.to_i + b.to_i).to_s
end
{% endhighlight %}

Run 'gauge specs' one last time. You should now have all passing tests.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
<figure class="highlight">
<pre>
<span style="color:#0AA"># Specification Heading
</span><span style="color:#A50">  ## Vowel counts in single word	</span><span style="color:#0A0"> ✔</span><span style="color:#0A0"> ✔</span>
<span style="color:#A50">  ## Vowel counts in multiple word	</span><span style="color:#0A0"> ✔</span><span style="color:#0A0"> ✔</span>

<span style="color:#0AA"># Add numbers
</span><span style="color:#A50">  ## Adding numbers	</span><span style="color:#0A0"> ✔</span>

Successfully generated html-report to => /home/user/gauge/reports/html-report
Specifications:	2 executed	2 passed	0 failed	0 skipped
Scenarios:	3 executed	3 passed	0 failed	0 skipped

Total time taken: 1.284s

</pre>
</figure>
</div>
</div>

If you would like to get more familiar with markdown and Gauge, they have a nice
cheat sheet to get you going. [http://getgauge.io/documentation/user/current/cheat_sheet/](http://getgauge.io/documentation/user/current/cheat_sheet/)
