---
layout: default
---
# Setting up CMake for Google Test

[![Build Status](https://travis-ci.org/testcookbook/google-test.svg?branch=master)](https://travis-ci.org/testcookbook/google-test.svg?branch=master)

Follow the code on [Github](https://github.com/testcookbook/google-test) while you read.

If you are new to C++ or CMake this can be somewhat of a daunting task on your own.  However if done correctly
it can save you quite a bit of heart ache in the end.  

As with many libraries you may need to use for your project you need a way to import the libraries resources
and link them correctly.  In this approach I don't want to maintain the Google Test libraries, I just want
to download them and use them when I need them.  You might want to also take note that Google Mock is now
mixed in with Google Test.  So you will be getting both tools on this build.

When we finish we will end up with a structure that looks something like the tree below.

```bash
$ tree
.
├── CMakeLists.txt
├── CMakeLists.txt.in
├── library.cpp
├── library.h
└── test
    ├── CMakeLists.txt
    ├── example.cpp
    ├── main.cpp
    └── simple.cpp
```

To start out lets create a new project folder.  You can name it something like TestExample.  Within it create
a file "CMakeLists.txt.in".  This file contains a basic config that we can use to download the latest source 
code for Google Tests and put it in the right location.

**CMakeLists.txt.in**
```
cmake_minimum_required(VERSION 2.8.2)

project(googletest-download NONE)

include(ExternalProject)
ExternalProject_Add(googletest
  GIT_REPOSITORY    https://github.com/google/googletest.git
  GIT_TAG           master
  SOURCE_DIR        "${CMAKE_BINARY_DIR}/googletest-src"
  BINARY_DIR        "${CMAKE_BINARY_DIR}/googletest-build"
  CONFIGURE_COMMAND ""
  BUILD_COMMAND     ""
  INSTALL_COMMAND   ""
  TEST_COMMAND      ""
)
```

Once we have that file we can move on to the CMakeLists.txt in the root directory of our TestExample project.

```
cmake_minimum_required(VERSION 3.8)
project(TestExample)

set(CMAKE_CXX_STANDARD 11)


# Download and unpack googletest at configure time
configure_file(CMakeLists.txt.in
        googletest-download/CMakeLists.txt)
execute_process(COMMAND ${CMAKE_COMMAND} -G "${CMAKE_GENERATOR}" .
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/googletest-download )
execute_process(COMMAND ${CMAKE_COMMAND} --build .
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/googletest-download )

# Prevent GoogleTest from overriding our compiler/linker options
# when building with Visual Studio
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Add googletest directly to our build. This adds
# the following targets: gtest, gtest_main, gmock
# and gmock_main
add_subdirectory(${CMAKE_BINARY_DIR}/googletest-src
        ${CMAKE_BINARY_DIR}/googletest-build)

# The gtest/gmock targets carry header search path
# dependencies automatically when using CMake 2.8.11 or
# later. Otherwise we have to add them here ourselves.
if (CMAKE_VERSION VERSION_LESS 2.8.11)
    include_directories("${gtest_SOURCE_DIR}/include"
            "${gmock_SOURCE_DIR}/include")
endif()

# Now simply link your own targets against gtest, gmock,
# etc. as appropriate


enable_testing()
add_subdirectory(test)

set(SOURCE_FILES library.cpp library.h)
add_library(TestExample ${SOURCE_FILES})

```

Now that we have the CMake config files done in the root directory we need to create a new directory
to house all of our tests.  

```
mkdir test
```

Within that directory create another file called CMakeLists.txt and fill in the following.

```
include_directories("${PROJECT_SOURCE_DIR}")

# First Simple Google Test
add_executable(simple simple.cpp)
target_link_libraries(simple gtest gmock_main)
add_test(NAME simple_test COMMAND simple)
```

Last but not least you can now create a new file in the test directory called "simple.cpp" and write
your first test. See writing a [unit test with Google Test](/book/cpp/unit-test-with-google-test.html)

Want to see it all together to play with check out this example on [Github](https://github.com/testcookbook/google-test).
