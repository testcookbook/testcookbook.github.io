# PHP Unit

PHPUnit is a unit testing framework in a XUnit architecture.  

## Getting Started.

The first thing you will need is PHPUnit installed locally.  I recommend using
composer.  This will allow you to download other dependencies if needed.

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

```
$ composer install
$ # or
$ php composer.phar install
```

After installing your dependencies you can begin to write some tests.  Lets start by writing some unit tests for a class that adds 2 numbers called Adder.

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

```
$ vendor/bin/phpunit adder_tests.php
```