---
layout: default
---
# Unit Test with Clojure

**Create a new App**

Command Line

```
lein new funapp
```

Leiningen will create a basic starting project for you that will look like the structure below.

```
.
├── CHANGELOG.md
├── LICENSE
├── README.md
├── doc
│   └── intro.md
├── project.clj
├── resources
├── src
│   └── funapp
│       └── core.clj
└── test
    └── funapp
        └── core_test.clj
```

Leiningen is package manage tool that will allow us a clean run and test interface. If you change into the funapp directory you can run “lein test”.

Command Line

```
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
```

Notice that when you run the project you start immediately with a failed test. The tests is in the core\_test.clj file and simply stating that it is expecting 0 to be equal to 1. Lets fix this test.

_test/funapp/core\_test.clj_

```clojure
(ns funapp.core-test
  (:require [clojure.test :refer :all]
            [funapp.core :refer :all]))

(deftest a-test
  (testing "FIXME, I fail."
    (is (= 0 1))))
```

Check out the last line of the test.

_test/funapp/core\_test.clj_

```clojure
(is (= 0 1))))
```

Witihin the last line there is a function “is” that asserts whether a its next argument resolves to true or false. If it is false it will result in a failing test. Let’s change that last line to look like.

_test/funapp/core\_test.clj_

```clojure
(is (= 1 1))))
```

This time when you run your tests you should see an output like.

Command Line

```
$ lein test

lein test funapp.core-test

Ran 1 tests containing 1 assertions.
0 failures, 0 errors.
```

## Test a function {#test-a-function}

Now that you have a basic build that is passing its tests we need to make it a little more useful. Lets say that in this funapp that I a function that will add up all the numbers in a list. We will start with a list of \(1 2 3\).

As with any TDD process lets write a basic failing test and add it to “core\_test.clj”.

_test/funapp/core\_test.clj_

```
(deftest addList-test
  (testing "Function should add up all numbers in the list"
    (is (= 6 (addList [1 2 3])))))
```

Command Line

```
$ lein test
Exception in thread "main" java.lang.RuntimeException: Unable to resolve symbol: addList in this context, compiling:(funapp/core_test.clj:11:14)
```

Failing is good. This particular failure is telling us that the function

Remember back from the tree diagram there is a src folder and underneath it is “funapp/core.clj”. Lets open that file up.

_funapp/core.clj_

```
(ns funapp.core)

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))
```

Within that file add a new function called addList that will sum up all the numbers in the list.

_funapp/core.clj_

```
(defn addList
  "This will add all the numbers in a list"
  [x]
  (reduce + x))
```

Try running your tests now.

Command Line

```
$ lein test

lein test funapp.core-test

Ran 2 tests containing 2 assertions.
0 failures, 0 errors.
```



