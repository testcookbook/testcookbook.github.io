---
layout: default
title:  "What is Gherkin"
description: "What is Gherkin?"
date:   2016-10-25 06:22:12 -0500
---
# What is Gherkin?

Gherkin is a business formatted DSL (Domain Specific Language) that is used to
describe how somethings behaves without actually implementing that functionality.

The format for a Gherkin file is done by defining a Feature, then a Scenario.
For Example.

{% highlight Gherkin %}
Feature: Describe what this feature is about.

  Scenario: Describe what the scenario will be about.
    Given I do something
    And do something else
    When this happens
    Then I get to do something new
{% endhighlight %}

Why would you ever want to write the Gherkin?  In a buisness format the Gherkin
file can be used in a variety of ways.  One of those ways is to have a common
language between the developer and the business. A business minded person can
use this format to describe a behavior that they would like out of the product.
Or the reverse can be true a developer can describe the functionality that they
will be implementing where the business person can understand.  

Now that I have this Gherkin file what can I do with it besides communicate with
the business people.  Once you have a behavior in mind that you need, you can
start the BDD process.  Write some step definitions to test your new application
based on the description on the DSL then write code to make it pass that behavior.

Once you have written steps and built your application based on those tests, now
you will have a living documentation for your application.  Depending on the
framework and language you use, you can create some interesting artifacts to go
along with the Gherkin.  For example by automating these tests you can record the
video of functionality or capture screenshots to help describe what is going on.  
These tools can be quite valuable to a new user of your application or maybe a new
team member.  As long as you keep up with your tests then you should have current
and reliable documentation for you application.

## Tools where you can use Gherkin
* [Cucumber](/book/cucumber/about_cucumber.html)
* [Lettuce](/book/lettuce/about_lettuce.html)
