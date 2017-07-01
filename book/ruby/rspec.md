---
layout: default
---
# RSpec

## Getting started.
Install rspec gem using gem command.

***Terminal***
```
$ gem install rspec
```

If you like to use bundler you can setup a Gemfile to look like.

***Gemfile***
```
source "https://rubygems.org"
gem "rspec"
```

## Your First test.
Lets say that we want to test a class that adds up numbers and has a function total. That function could look like.

```ruby
class Adder
  def initialize(a, b)
    @a = a
    @b = b
  end

  def total
    @a + @b
  end
end
```

Now that we have what we are going to test.  We need to have a basic layout of our test ready.

```ruby
RSpec.describe Adder do
  describe "adds numbers" do
    it "Adder total returns correct value" do

    end
  end
end
```

Notice that RSpec works in a describe and it format.  The first section tells RSpec that we are going to test the Adder function.  The second describe tells a high level story of what it will cover.  Lastly the "it" will test a specific functionality that is a part of the describe.

Next we need to load up a couple of numbers to the Adder function and then create an assertion to what the correct total.

```ruby
RSpec.describe Adder do
  describe "adds numbers" do
    it "Adder total returns correct value" do
        adder = Adder.new(3,5)
        expect(adder.total).to eq(8)
    end
  end
end
```

See it all together

***spec.rb***
```ruby
class Adder
  def initialize(a, b)
    @a = a
    @b = b
  end

  def total
    @a + @b
  end
end

RSpec.describe Adder do
  describe "adder" do
    it "Adder total returns correct value" do
      adder = Adder.new(3,5)
      expect(adder.total).to eq(8)
    end
  end
end
```

## Run your test

***Terminal***
```
$ rspec spec.rb
.

Finished in 0.00091 seconds (files took 0.09214 seconds to load)
1 example, 0 failures
```
