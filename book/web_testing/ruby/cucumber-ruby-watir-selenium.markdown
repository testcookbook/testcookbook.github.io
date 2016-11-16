---
layout: default
title:  "Cucumber using Ruby and Watir"
description: "Cucumber Ruby and Watir implementation."
---

# Cucumber using Ruby and Watir

Cucumber with Ruby I believe is one of the easiest forms of behavior test
automation.  Getting started we first need a basic directory structure.

```
- features
  - support
  - step_definitions
```

Once you have created your directory structure you will need to create a
Gemfile.  If you are unfamiliar with Ruby a Gemfile holds the names and versions
of packages that can be downloaded to allow your project to work.


<header class="cm1 w3-blue">
  {% include fileIcon.html %}
  Gemfile
</header>

```ruby
source 'https://rubygems.org'

gem 'cucumber'
gem 'rspec-expectations'
gem 'watir-webdriver'
gem 'selenium-webdriver'
```

To install all the needed packages you can now do the following on the command
line.


    <header class="cm1 w3-grey">
      {% include cliIcon.html%}
      Command Line
    </header>


```
gem install bundler
bundle install
```



Now we need to setup an environment for cucumber.  To do this you can create a
'env.rb' file in the support directory.  This file will become more useful for
different configuration items later on.  For now we just need a small bit of
code.

    <header class="cm1 w3-blue">
      {% include fileIcon.html %}
      env.rb
    </header>


```ruby
require 'watir-webdriver'
```



If you have done everything right you should have the basic structure for a
cucumber test suite.  It should run however you do not have an tests just yet.
Lets create a new feature file called 'testCookbook.feature'.
{% include testCookbookFeature.html %}

Now try running your cucumber suite.  To do so run the command below on the
command line.  When it runs you should see some yellow text showing that you
need step definitions.


    <header class="cm1 w3-grey">
      {% include cliIcon.html%}
      Command Line
    </header>


```
bundle exec cucumber
```



Building step definitions can be done by copying the template in yellow from the
command line or building your own regular expression definition to match. For
this example create a file called steps.rb in the step_definitions directory.


    <header class="cm1 w3-blue">
      {% include fileIcon.html %}
      steps.rb
    </header>


```ruby
Given(/^I visit Test Cookbook website$/) do
  @browser.goto 'http://www.testcookbook.com'
end

Then(/^I see title Test Cookbook$/) do
  expect(@browser.title).to eq("Test Cookbook")
end
```



Now try running one more time.  This time you should see some errors.  We need
to build us some small hooks that will take care of setup and teardown of the
browser.  Lets make a new file in the support directory called 'hooks.rb'.


    <header class="cm1 w3-blue">
    {% include fileIcon.html %}
      hooks.rb
    </header>


```ruby
Before do
  @browser = Watir::Browser.new
end

After do
  @browser.close
end
```



Last try and this time it should work.  Run your Cucumber suite and you should
start seeing the feature file you wrote in a bright green.  If there was
something wrong you will get text in red.  The goal is to make all the tests
look the color of a cucumber.  
