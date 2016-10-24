---
layout: default
title:  "Cucumber + Selenium Web Driver for Java"
description: "Running Cucumber with Java JVM and Selenium Web Driver."
---
# Cucumber + Selenium Web Driver for Java

## Creating Maven pom.xml
---
Initialize a pom.xml file either using the generate function or on your own.
Then add the dependencies below.

{% highlight xml %}
<dependencies>
  <dependency>
    <groupId>info.cukes</groupId>
    <artifactId>cucumber-junit</artifactId>
    <version>1.2.4</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>info.cukes</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>1.2.4</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>2.53.1</version>
  </dependency>
</dependencies>
{% endhighlight %}

## Files Structure
---
Once you have created a pom.xml file the next important step is the Structure
of the files. You will need 2 main folders to start out.  

{% highlight text %}
src/test/java/com/program/test/step_definitions
src/test/resources/features
{% endhighlight %}

Notice on the step definitions folder.  It says "/com/program/test/".  This can
and probably should be changed to your actual program structure.  If just using
as standalone tests then it should be fine.

## Creating a feature.
---
In the "resources/features" directory you will add your feature files in Gherkin
format.  In the case of this exercise we can use.
{% include testCookbookFeature.html %}

For more information about Gherkin you can refer back to the Gherkin chapter.

## Writing code to make things pass.
---
In order to make use of the Gherkin feature is to write some code that will do
3 very important things.  

1. Build a runner to tell Cucumber how to act and report.
2. Create a hook to start the browser instance.
3. Build step definitions to translate the plain english Gherkin to actual code.

### Runner
---
Simple enough right?  Well lets start with step 1 and create the runner. For my
example I create a file called RunCukesTest.java within the step_definitions
directory.
<div class="w3-card">
    <header class="w3-container w3-blue">
      {% include fileIcon.html %}
      RunCukesTest.java
    </header>

    <div class="w3-container">
{% highlight Java %}
package step_definitions;

import cucumber.api.junit.Cucumber;
import cucumber.api.CucumberOptions;

import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
  features = "classpath:features",
  plugin = {"pretty", "html:target/cucumber-html-report"},
  tags = {}
)

public class RunCukesTest {}
{% endhighlight %}
  </div>
</div>

### Hooks
---
After creating the runner, we need to build some hooks.  These hooks will help
us along they way for setup and tear down for out tests. Lets create a file
called Hooks.java
<div class="w3-card">
    <header class="w3-container w3-blue">
      {% include fileIcon.html %}
      RunCukesTest.java
    </header>

    <div class="w3-container">
{% highlight Java %}
package step_definitions;

import java.net.MalformedURLException;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriverException;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import cucumber.api.Scenario;
import cucumber.api.java.After;
import cucumber.api.java.Before;

public class Hooks{
public static WebDriver driver;


  @Before
  public void openBrowser() throws MalformedURLException {
    driver = new FirefoxDriver();
    driver.manage().deleteAllCookies();
    driver.manage().window().maximize();
  }

  @After
  public void embedScreenshot(Scenario scenario) {

    if(scenario.isFailed()) {
      try {
        scenario.write("Current Page URL is " + driver.getCurrentUrl());
        byte[] screenshot = ((TakesScreenshot)driver).getScreenshotAs(OutputType.BYTES);
        scenario.embed(screenshot, "image/png");
      } catch (WebDriverException somePlatformsDontSupportScreenshots) {
        System.err.println(somePlatformsDontSupportScreenshots.getMessage());
      }

    }
    driver.quit();
  }

}
{% endhighlight %}
</div>
</div>

### Step Definitions
---
Last but certainly not the least we need a step definition called
TestCookbookPage.java

<div class="w3-card">
    <header class="w3-container w3-blue">
      {% include fileIcon.html %}
      TestCookbookPage.java
    </header>

    <div class="w3-container">
{% highlight Java %}
package step_definitions;

import static org.junit.Assert.assertTrue;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;


public class TestCookbookPage {
  public WebDriver driver;

  public TestCookbookPage() {

    driver = Hooks.driver;
  }

  @Given("^I visit Test Cookbook website$")
    public void i_visit_Test_Cookbook_website() throws Throwable {
      driver.get("http://www.testcookbook.com");
    }

  @Then("^I see title Test Cookbook$")
    public void i_see_title_Test_Cookbook() throws Throwable {
      assertTrue(driver.getTitle().contains("Test Cookbook"));
    }

}
{% endhighlight %}
  </div>
</div>

## Working Example
---
[https://github.com/testcookbook/java-cucumber-selenium](https://github.com/testcookbook/java-cucumber-selenium)
