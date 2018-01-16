---
layout: default
---
# C Unit Testing with cmocka {#c-unit-testing-with-cmocka}

**Ingredients**

* C compiler
* [cmocka](https://cmocka.org/)

**Bake Time**

* 10 min

**Instructions**

Create a new file called *test.c*. This will be a simple src file to create a basic test.

```c
#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include <cmocka.h>

static void failing_test() {
	assert_false(1 != 2);
}

int main(void) {
	const struct CMUnitTest tests[] = {
		cmocka_unit_test(failing_test),
	};
	return cmocka_run_group_tests(tests, NULL, NULL);
}
```

Build your tests

```
$ gcc -o test test.c -l cmocka -L /usr/local/lib
```

Run your tests

```
$ ./test
```

**Using a Makefile**
```
buildTests : createBuildDir
	gcc -o build/test test.c -l cmocka -L /usr/local/lib

createBuildDir :
	mkdir -p build

test :
	./build/test

clean :
	rm -Rf build
```
