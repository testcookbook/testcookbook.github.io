---
layout: default
---
# Unit Test with Google Test

Creating your first test.  

```
#include "gtest/gtest.h"
   
TEST(One, EqualsOne)
{
    EXPECT_EQ(1, 1);
}
```

As far as tests go this one is rather quick and easy to write, but it also doesn't do much. 
This particular test checks to see if 1 equals 1.  Let's see if we can write a test that checks
if a function called add returns the correct value.

```
#include "gtest/gtest.h"

int add(int a, int b) {
    return a + b;
}
   
TEST(add_function, Two_Plus_Two_Equals_Four)
{
    EXPECT_EQ(add(2, 2), 4);
}
```

Want to see it all together to play with check out this example on [Github](https://github.com/testcookbook/google-test).