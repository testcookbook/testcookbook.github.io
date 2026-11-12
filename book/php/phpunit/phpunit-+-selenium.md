---
layout: default
---
# PHPUnit + Selenium

This chapter drives a real browser from PHPUnit tests using
[php-webdriver](https://github.com/php-webdriver/php-webdriver). Read [PHPUnit](/book/php/phpunit.html)
first if you have not used it yet.

The code here was written for php-webdriver 1.x and Selenium 4. A complete example project is in
the [PHPUnit Selenium repo on GitHub](https://github.com/testcookbook/php-phpunit-selenium).

## Start a Selenium server

The easiest way to get a browser is the standalone Chrome image from the Selenium project. Run it
with Docker:

```
$ docker run -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome
```

## Install the dependencies

```
$ composer require --dev phpunit/phpunit php-webdriver/webdriver
```

## A first browser test

Create `tests/ExampleTest.php`:

```php
<?php

use Facebook\WebDriver\Remote\DesiredCapabilities;
use Facebook\WebDriver\Remote\RemoteWebDriver;
use Facebook\WebDriver\WebDriverBy;
use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    private $driver;

    protected function setUp(): void
    {
        $this->driver = RemoteWebDriver::create(
            'http://localhost:4444',
            DesiredCapabilities::chrome()
        );
    }

    protected function tearDown(): void
    {
        $this->driver->quit();
    }

    public function testPageTitle()
    {
        $this->driver->get('https://example.com');
        $this->assertEquals('Example Domain', $this->driver->getTitle());
    }

    public function testHeadingText()
    {
        $this->driver->get('https://example.com');
        $heading = $this->driver->findElement(WebDriverBy::tagName('h1'));
        $this->assertEquals('Example Domain', $heading->getText());
    }
}
```

Each test gets a fresh browser in `setUp()`, and `tearDown()` closes it so tests do not leak state
into each other.

## Run the tests

```
$ vendor/bin/phpunit tests
```

PHPUnit prints a dot for each passing test. A failure shows the assertion that did not match and
the expected and actual values.
