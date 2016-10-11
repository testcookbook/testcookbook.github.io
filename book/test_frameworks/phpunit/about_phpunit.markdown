---
layout: default
title:  "PHP Unit"
---
# PHP Unit

PHPUnit is a unit testing framework in a XUnit architecture.  

## Getting Started.

The first thing you will need is PHPUnit installed locally.  I recommend using
composer.  This will allow you to download other dependencies if needed.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  composer.json
</header>

<div class="w3-container">
{% highlight json %}
{
  "name": "testcookbook/phpunit",
  "authors": [
    {
      "name": "Your Name",
      "email": "your@email.com"
    }
  ],
  "require-dev": {
    "phpunit/phpunit": "^5.5"
  },
  "require": {
  }
}
{% endhighlight %}
</div>
</div>

To install you can run.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ composer install
$ # or
$ php composer.phar install
{% endhighlight %}
</div>
</div>

After installing your dependencies you can begin to write some tests.  Lets
start by writing some unit tests for a class that adds 2 numbers called Adder.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  adder_tests.php
</header>

<div class="w3-container">
{% highlight php %}
<?php
use PHPUnit\Framework\TestCase;

require('adder.php');

class AdderTest extends TestCase
{
  public function numberCanBeAdded()
  {
    $adder = new Adder(2, 3);
    $total = $adder->getTotal();

    // Assert
    $this->assertEquals(5, $total);
  }
}
?>
{% endhighlight %}
</div>
</div>

Now lets create a basic class to make the test pass.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  adder.php
</header>

<div class="w3-container">
{% highlight php %}
<?php
class Adder
{
  private $a;
  private $b;

  public function __construct($a, $b)
  {
    $this->a = $a;
    $this->b = $b;
  }

  public function getTotal()
  {
    return $this->a + $this->b;
  }

}
?>
{% endhighlight %}
</div>
</div>

To run your tests.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ vendor/bin/phpunit adder_tests.php
{% endhighlight %}
</div>
</div>
