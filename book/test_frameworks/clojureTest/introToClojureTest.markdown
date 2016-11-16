---
layout: default
title:  "Introduction to Clojure Test"
description: "Introduction to Clojure Test"
---
# Introduction to Clojure Test

**Create a new App**

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight shell %}
$ lein new funapp
{% endhighlight %}
</div>
</div>

Leiningen will create a basic starting project for you that will look like the
structure below.

```
.
├── CHANGELOG.md
├── LICENSE
├── README.md
├── doc
│   └── intro.md
├── project.clj
├── resources
├── src
│   └── funapp
│       └── core.clj
└── test
    └── funapp
        └── core_test.clj
```

Leiningen is package manage tool that will allow us a clean run and test
interface. If you change into the funapp directory you can run "lein test".

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
$ lein test

lein test funapp.core-test

lein test :only funapp.core-test/a-test

FAIL in (a-test) (core_test.clj:7)
FIXME, I fail.
expected: (= 0 1)
  actual: (not (= 0 1))

Ran 1 tests containing 1 assertions.
1 failures, 0 errors.
Tests failed.
{% endhighlight %}
</div>
</div>

Notice that when you run the project you start immediately with a failed test.
The tests is in the core_test.clj file and simply stating that it is expecting
0 to be equal to 1.  Lets fix this test.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  test/funapp/core_test.clj
</header>

<div class="w3-container">
{% highlight clojure %}
(ns funapp.core-test
  (:require [clojure.test :refer :all]
            [funapp.core :refer :all]))

(deftest a-test
  (testing "FIXME, I fail."
    (is (= 0 1))))

{% endhighlight %}
</div>
</div>

Check out the last line of the test.

```clojure
(is (= 0 1))))
```

Witihin the last line there is a function "is" that asserts whether a its next
argument resolves to true or false.  If it is false it will result in a failing
test.  Let's change that last line to look like.

```clojure
(is (= 1 1))))
```

This time when you run your tests you should see an output like.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
$ lein test

lein test funapp.core-test

Ran 1 tests containing 1 assertions.
0 failures, 0 errors.
{% endhighlight %}
</div>
</div>

## Test a function

Now that you have a basic build that is passing its tests we need to make it
a little more useful.  Lets say that in this funapp that I a function that will
add up all the numbers in a list.  We will start with a list of (1 2 3).

As with any TDD process lets write a basic failing test and add it to
"core_test.clj".

```clojure
(deftest addList-test
  (testing "Function should add up all numbers in the list"
    (is (= 6 (addList [1 2 3])))))
```

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
$ lein test
Exception in thread "main" java.lang.RuntimeException: Unable to resolve symbol: addList in this context, compiling:(funapp/core_test.clj:11:14)
{% endhighlight %}
</div>
</div>

Failing is good.  This particular failure is telling us that the function



Remember back from the tree diagram there is a src folder and underneath it is
"funapp/core.clj".  Lets open that file up.

<div class="w3-card">
<header class="w3-container w3-blue">
  {% include fileIcon.html%}
  funapp/core.clj
</header>

<div class="w3-container">
{% highlight clojure %}
(ns funapp.core)

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))
{% endhighlight %}
</div>
</div>


Within that file add a new function called addList that will sum up all the
numbers in the list.

{% include clojure/introClojureTest/addList.markdown %}

Try running your tests now.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>

<div class="w3-container">
{% highlight text %}
$ lein test

lein test funapp.core-test

Ran 2 tests containing 2 assertions.
0 failures, 0 errors.
{% endhighlight %}
</div>
</div>
