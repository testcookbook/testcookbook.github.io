---
layout: default
title:  "Cucumber using Ruby and Watir
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

{% highlight gemfile %}
source 'https://rubygems.org'

gem 'cucumber'
gem 'rspec-expectations'
gem 'watir-webdriver'
gem 'selenium-webdriver'
{% endhighlight %}