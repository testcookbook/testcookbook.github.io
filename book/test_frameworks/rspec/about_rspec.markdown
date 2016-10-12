---
layout: default
title:  "RSpec"
---
# RSpec

## Getting started.
Install rspec gem using gem command.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ gem install rspec
{% endhighlight %}
</div>
</div>

If you like to use bundler you can setup a Gemfile to look like.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  Gemfile
</header>

<div class="w3-container">
{% highlight language %}
source "https://rubygems.org"
gem "rspec"
{% endhighlight %}
</div>
</div>

## Your First test.
Lets say that we want to test a class that adds up numbers and has a function
total. That function could look like.

{% highlight ruby %}
class Adder
  def initialize(a, b)
    @a = a
    @b = b
  end

  def total
    @a + @b
  end
end
{% endhighlight %}

Now that we have what we are going to test.  We need to have a basic layout of
our test ready.

{% highlight ruby %}
RSpec.describe Adder do
  describe "adds numbers" do
    it "Adder total returns correct value" do

    end
  end
end
{% endhighlight %}

Notice that RSpec works in a describe and it format.  The first section tells
RSpec that we are going to test the Adder function.  The second describe tells
a high level story of what it will cover.  Lastly the "it" will test a specific
functionality that is a part of the describe.

Next we need to load up a couple of numbers to the Adder function and then
create an assertion to what the correct total.

{% highlight ruby %}
RSpec.describe Adder do
  describe "adds numbers" do
    it "Adder total returns correct value" do
        adder = Adder.new(3,5)
        expect(adder.total).to eq(8)
    end
  end
end
{% endhighlight %}

See it all together

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  spec.rb
</header>

<div class="w3-container">
{% highlight ruby %}
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
{% endhighlight %}
</div>
</div>

## Run your test
<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ rspec spec.rb
.

Finished in 0.00091 seconds (files took 0.09214 seconds to load)
1 example, 0 failures
{% endhighlight %}
</div>
</div>
