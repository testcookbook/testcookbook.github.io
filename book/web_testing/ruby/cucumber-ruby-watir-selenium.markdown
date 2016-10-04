---
layout: default
title:  "Cucumber using Ruby and Watir"
---

# Cucumber using Ruby and Watir

Cucumber with Ruby I believe is one of the easiest forms of behavior test 
automation.  Getting started we first need a basic directory structure.

{% highlight text %}
- features
  - support
  - step_definitions
{% endhighlight %}

Once you have created your directory structure you will need to create a 
Gemfile.  If you are unfamiliar with Ruby a Gemfile holds the names and versions
of packages that can be downloaded to allow your project to work.

<div class="w3-card">
    <header class="w3-container w3-blue">
      <h4>Gemfile</h4>
    </header>
    
    <div class="w3-container">
{% highlight ruby %}
source 'https://rubygems.org'

gem 'cucumber'
gem 'rspec-expectations'
gem 'watir-webdriver'
gem 'selenium-webdriver'
{% endhighlight %}
    </div>
</div>

To install all the needed packages you can now do the following on the command
line. 

<div class="w3-card">
    <header class="w3-container w3-grey">
      <h4>Command Line</h4>
    </header>
    
    <div class="w3-container">
{% highlight bash %}
gem install bundler
bundle install
{% endhighlight %}
    </div>
</div>

Now we need to setup an environment for cucumber.  To do this you can create a
'env.rb' file in the support directory.  This file will become more useful for 
different configuration items later on.  For now we just need a small bit of 
code.
<div class="w3-card">
    <header class="w3-container w3-blue">
      <h4>env.rb</h4>
    </header>
    
    <div class="w3-container">
{% highlight ruby %}
require 'watir-webdriver'
{% endhighlight %}
    </div>
</div>

If you have done everything right you should have the basic structure for a 
cucumber test suite.  It should run however you do not have an tests just yet.
Lets create a new feature file called 'testCookbook.feature'.
<div class="w3-card">
    <header class="w3-container w3-blue">
      <h4>testCookbook.feature</h4>
    </header>
    
    <div class="w3-container">
{% highlight Gherkin %}
Feature: Test Cookbook Home Page

  Scenario: Test Cookbook Title Description
    Given I visit Test Cookbook website
    Then I see title Test Cookbook
{% endhighlight %}
    </div>
</div>

Now try running your cucumber suite.  To do so run the command below on the 
command line.  When it runs you should see some yellow text showing that you
need step definitions.

<div class="w3-card">
    <header class="w3-container w3-grey">
      <h4>Command Line</h4>
    </header>
    
    <div class="w3-container">
{% highlight bash %}
bundle exec cucumber
{% endhighlight %}
    </div>
</div>

Building step definitions can be done by copying the template in yellow from the
command line or building your own regular expression definition to match. For 
this example create a file called steps.rb in the step_definitions directory.

<div class="w3-card">
    <header class="w3-container w3-blue">
      <h4>steps.rb</h4>
    </header>
    
    <div class="w3-container">
{% highlight ruby %}
Given(/^I visit Test Cookbook website$/) do
  @browser.goto 'http://www.testcookbook.com'
end

Then(/^I see title Test Cookbook$/) do
  expect(@browser.title).to eq("Test Cookbook")
end
{% endhighlight %}
    </div>
</div>

Now try running one more time.  This time you should see some errors.  We need
to build us some small hooks that will take care of setup and teardown of the 
browser.  Lets make a new file in the support directory called 'hooks.rb'.

<div class="w3-card">
    <header class="w3-container w3-blue">
      <h4>hooks.rb</h4>
    </header>
    
    <div class="w3-container">
{% highlight ruby %}
Before do 
  @browser = Watir::Browser.new
end

After do
  @browser.close
end
{% endhighlight %}
    </div>
</div>

Last try and this time it should work.  Run your Cucumber suite and you should
start seeing the feature file you wrote in a bright green.  If there was 
something wrong you will get text in red.  The goal is to make all the tests 
look the color of a cucumber.  