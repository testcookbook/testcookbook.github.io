---
layout: default
---
# Ruby + Cucumber
[![Build Status](https://travis-ci.org/testcookbook/ruby-cucumber.svg?branch=master)](https://travis-ci.org/testcookbook/ruby-cucumber.svg?branch=master)

All the source for this lesson is on [Github](https://github.com/testcookbook/ruby-cucumber).

Cucumber is a behavior driven development test framework.  This framework was designed to allow for living documentation, business readability, and allow the team a focus on what the customer wants.

Now imagine you are on a development team creating new application.  You can grab the 3 amigos (developer, tester, product owner or stake holder).  While you sit together you talk about what the acceptance criteria is for you application.  It may take a while for each of the members to agree on what the scope is but you will get there.  Once you have the criteria you write them in a format that is both readable to you and the other members of the team.

### Gherkin
[Gherkin](/book/common-automation-concepts/gherkin.html) is readable formatted file that will allow other members of the team, to understand what the acceptance criteria is, and also provide that living documentation of your application.  Once this file or feature is written, you can run the tests with Cucumber and determine how far along you have come with a given criteria. For example.

***testCookbook.feature***
```Gherkin
Feature: Test Cookbook Home Page

  Scenario: Test Cookbook Title Description
    Given I visit Test Cookbook website
    Then I see title Test Cookbook
```

### How to get started?

Getting started with Cucumber is not usually a complicated feat.  The first step is picking a programming language that is appropriate for you.  In some cases this could be a programming language that you are strong in, or in other cases you might want to integrate the tests within your application suite and use the
same language.

To get started with this example we will use Ruby and layout some basics. A normal directory setup would look something like.

```
.
├── features
│   ├── test1.feature
│   ├── test2.feature
│   ├── step_definitions
│   │   └── steps.rb
│   └── support
│       ├── env.rb
│       └── hooks.rb
└── Gemfile
```

The features directory would contain your feature files.  These feature files will be written in a Gherkin style format.  

Step definitions will be code that executes the different steps described in the feature files.  In this case we are making a 'steps.rb'.  You could name it anything that is appropriate for you to understand whats in the file.  One nice thing about using Cucumber for Ruby is that any Ruby file within the step_definitions can house the definitions.

The support directory should have at least 'env.rb'.  This file is used to setup the global configurations for your test suite.  One other thing that we included in the support directory is the 'hooks.rb'.  This will allow you to create some basic steps that could run before or after any given scenario.

The last file you see in the diagram is a Gemfile.  If you are not familiar with Ruby this is a package file that will help you download the correct gems to run your test suite.

For this exercise we are going to keep to as close to bare minimal as possible so that you can learn what is going on.  Once you move to more complicated scenarios like testing websites with Selenium you will probably want to create a directory for page objects and flows.  Things that seem repetitive within your
tests your want to use the DRY method when developing.  DRY means don't repeat yourself.

Now lets create some directories and try out some Cucumber.  You will also need Ruby for these examples to work.  If you have never installed or used Ruby, check out. [https://www.ruby-lang.org/](https://www.ruby-lang.org/)

***Terminal - Mac / Linux***
```
$ mkdir cucumber
$ cd cucumber
$ gem install cucumber
$ gem install rspec-expectations
$ cucumber --init
```

Windows is similar but you need to make sure that your slashes face the right direction.  The homedir below will be your Windows user name.  You can create the cucumber directory where ever you would like.  You will also need to make sure on windows that 'cucumber' and 'gem' binaries are in your PATH variable.

***Terminal - Windows***
```
C:\Users\homedir> mkdir cucumber
C:\Users\homedir\cucumber> cd cucumber
C:\Users\homedir\cucumber> gem install cucumber
C:\Users\homedir\cucumber> gem install rspec-expectations
C:\Users\homedir\cucumber> cucumber --init
```

Now create a new file within the features directory called 'test1.feature'

***features/test1.feature***

```gherkin
Feature: Test 1

  Scenario: Add 2 Numbers
    Given There are numbers 2 and 3
    When added together
    Then they equal 5
```

Lets try running cucumber. You should get an output similar to this below.

***Terminal***
```
$ cucumber

Feature: Test 1

  Scenario: Add 2 Numbers           # features/test1.feature:3
    Given There are numbers 2 and 3 # features/test1.feature:4
    When added together             # features/test1.feature:5
    Then they equal 5               # features/test1.feature:6

1 scenario (1 undefined)
3 steps (3 undefined)
0m0.023s

You can implement step definitions for undefined steps with these snippets:

Given("There are numbers {int} and {int}") do |int, int2|
  pending # Write code here that turns the phrase above into concrete actions
end

When("added together") do
  pending # Write code here that turns the phrase above into concrete actions
end

Then("they equal {int}") do |int|
  pending # Write code here that turns the phrase above into concrete actions
end
```

More than likely when you ran cucumber it printed the text above and much of it should be yellow.  Some terminals may not support ascii color so it might be all the same color.  The yellow text signifies steps within the defined feature that are not yet implemented yet.  When using cucumber in Ruby we can actually copy the suggested code and put them into a 'steps.rb' file.

***features/step_definitions/steps.rb***
```ruby
Given("There are numbers {int} and {int}") do |int, int2|
  @a = int
  @b = int2
end

When("added together") do
  @total = @a + @b
end

Then("they equal {int}") do |int|
    expect(@total).to eq(int)
end
```

Try running cucumber again.

***Terminal***
```
$ cucumber

Feature: Test 1

  Scenario: Add 2 Numbers           # features/test1.feature:3
    Given There are numbers 2 and 3 # features/step_definitions/steps.rb:1
      TODO (Cucumber::Pending)
      ./features/step_definitions/steps.rb:2:in `/^There are numbers (\d+) and (\d+)$/'
      features/test1.feature:4:in `Given There are numbers 2 and 3'
    When added together             # features/step_definitions/steps.rb:5
    Then they equal 5               # features/step_definitions/steps.rb:9

1 scenario (1 pending)
3 steps (2 skipped, 1 pending)
0m0.025s
```



This time when you ran cucumber there were step definitions that have some code to them.  Each one of the steps was set to just return pending.  If a step returns pending it will usually be yellow and all the steps below it are a light blue.  They are blue because they could not be run yet.  The scenario ended after the first pending.

We need to define some code rather than return pending.  In the first step we are accepting 2 numbers arg1 and arg2.  For this example we need to make those numbers accessible to other tests. Lets make the function look like.

```ruby
Given("There are numbers {int} and {int}") do |int, int2|
  @a = int
  @b = int2
end
```
You will probably notice the to_i after the arg1 and arg2.  This just changes the value to be an integer.  The @ sign in front of a and b is significant as well.  This means those become instance variables and are available across the class.  If they were without the @ sign we would not be able to access them in the other steps.  

Now when you run cucumber you should get a green line for the first step.  The closer the color matches to a cucumber the closer you are to success.  Lets go ahead and fix up the other 2 test definitions.

```ruby
When("added together") do
  @total = @a + @b
end

Then("they equal {int}") do |int|
    expect(@total).to eq(int)
end
```

Before you decide to run cucumber again we really need to add a small bit of code to the 'env.rb' file.  This file is used to setup the cucumber world or global settings that you will use within your tests.  For our tests to have a real value the assert statements need to work.  Otherwise you aren't really testing anything.

***features/support/env.rb***
```ruby
  #With the use of rspec-expectations and latest cucumber no world variables are needed here
  for this example.
```

Now when you run cucumber you should get all green.


***Terminal***

```
$ cucumber

Feature: Test 1

  Scenario: Add 2 Numbers           # features/test1.feature:3
    Given There are numbers 2 and 3 # features/step_definitions/steps.rb:1
    When added together             # features/step_definitions/steps.rb:6
    Then they equal 5               # features/step_definitions/steps.rb:10

1 scenario (1 passed)
3 steps (3 passed)
0m0.028s
```

Now remember back a short while ago when we said that if we do not assert anything you are not really testing anything.  All Green tests can be a false positive, which is something you do not want.  For example in the 'steps.rb' file. Put a # sign in front of the assert statement like so.

```ruby
#expect(@total).to eq(int)
```

When you run cucumber this time it is still all green.  You could change those numbers in the previous steps to any number you want.  It will always pass. Make sure that when you write your tests they provide value and actually assert for something.
