---
layout: default
title:  "Introduction to Bash testing with Bats"
description: "Introduction to Bash testing with Bats - Bash Automated Testing System"
---
# Introduction to Bash Automated Testing System (Bats)

**Equality**

```bash
#!/usr/bin/env bats

@test "Numbers Equal" {
    result="2"
    [ "$result" -eq 2 ]
}

@test "Numbers Less Than" {
    result="2"
    [ "$result" -lt 4 ]
}

@test "Numbers Greater Than" {
    result="6"
    [ "$result" -gt 4 ]
}

@test "String contains family" {
    [[ "this family is cool" == *"family"* ]]
}
```

**System Tests**

Validating what your hostname is.

```bash
@test "Hostname is testcookbook" {
    result="$(hostname)"
    [ "$result" == "testcookbook" ]
}
```

Test for IP Address using a conditional if to skip if the OS is not a Mac.

```bash
@test "IP addres is 192.168.1.3" {
#This is for Mac only
    if [ $(uname) != "Darwin" ]; then
        skip "This test is only accurate for Mac"
    fi
    result="$(ipconfig getifaddr en0)"
    [ "$result" == "192.168.1.3" ]
}
```
