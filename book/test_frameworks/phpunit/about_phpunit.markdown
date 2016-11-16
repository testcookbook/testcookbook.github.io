---
layout: default
title:  "PHP Unit"
description: "Getting started with PHPUnit tests."
---
# PHP Unit

PHPUnit is a unit testing framework in a XUnit architecture.  

## Getting Started.

The first thing you will need is PHPUnit installed locally.  I recommend using
composer.  This will allow you to download other dependencies if needed.


<header class="cm1 w3-blue">
  {% include fileIcon.html%}
  composer.json
</header>


```json
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
```



To install you can run.


<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>


```
$ composer install
$ # or
$ php composer.phar install
```



After installing your dependencies you can begin to write some tests.  Lets
start by writing some unit tests for a class that adds 2 numbers called Adder.


<header class="cm1 w3-blue">
  {% include fileIcon.html%}
  adder_tests.php
</header>


```php
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
```



Now lets create a basic class to make the test pass.


<header class="cm1 w3-blue">
  {% include fileIcon.html%}
  adder.php
</header>


```php
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
```



To run your tests.


<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>


```
$ vendor/bin/phpunit adder_tests.php
```
