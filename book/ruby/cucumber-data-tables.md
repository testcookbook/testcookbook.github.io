---
layout: default
---

# Cucumber Data Tables using Ruby

[![Build Status](https://travis-ci.org/testcookbook/ruby-cucumber.svg?branch=master)](https://travis-ci.org/testcookbook/ruby-cucumber.svg?branch=master)

All the source for this lesson is on [Github](https://github.com/testcookbook/ruby-cucumber).

Data tables are text structures built with pipes | and even spaces following right after the step 
that is written in the feature file.  By default all tables are 2 dimensional arrays.  During this 
lesson we will look at how to process these arrays in 3 different ways.  Horizontally, vertically 
and full 2D array.

## Horizontal Data Table

*features/data-table.feature*
```gherkin
Scenario: Add numbers in a horizontal tables
    Given a list of numbers horizontally
        | 1 | 3 | 5 |
    Then the total for the horizontal list is 9
```

*features/step_definitions/data_table.rb*
```ruby
Given("a list of numbers horizontally") do |table|
    @list = table.raw
end

Then("the total for the horizontal list is {int}") do |int|
    total = 0
    @list.first.each { |a| total += a.to_i }
    expect(total).to eq(int)
end
```

## Vertical Data Table
```gherkin
Scenario: Add numbers in a vertical table
    Given a list of numbers vertically
        | 1 |
        | 2 |
        | 4 |
    Then the total for the vertical list is 7
```

```ruby
Given("a list of numbers vertically") do |table|
    @list = table.raw
end

Then("the total for the vertical list is {int}") do |int|
  total = 0
  @list.each { |a| total += a.first.to_i }
  expect(total).to eq(int)
end
```

## 2 Dimensional
```gherkin
Scenario: Add numbers in a 2D array
    Given a list of numbers in 2D array
        | 1 | 3 | 5 |
        | 2 | 6 | 3 |
        | 4 | 2 | 2 |
    Then the total for all numbers in 2D array is 28
```

```ruby
Given("a list of numbers in 2D array") do |table|
  @list = table.raw
end

Then("the total for all numbers in 2D array is {int}") do |int|
  total = 0
  @list.each { |a| a.each { |b| total += b.to_i } }
  expect(total).to eq(int)
end
```

If you wanted to [DRY](/book/common-automation-concepts/dry.html) this code up a little bit.  You could actually use the same Given 
statement for all of these 3 scenarios.
