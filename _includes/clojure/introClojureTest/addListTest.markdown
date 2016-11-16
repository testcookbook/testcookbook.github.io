```clojure
(deftest addList-test
  (testing "Function should add up all numbers in the list"
    (is (= 6 (addList [1 2 3])))))
```