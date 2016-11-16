---
layout: default
title:  "Create a NodeJS project"
description: "Create a NodeJS project"
date:   2016-11-08 08:52:00 -0500
---
# Create a NodeJS project

Basic steps to creating a NodeJS package.json file.  


<header class="cm1 w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>


```
$ mkdir test
$ npm init
name: (test)
version: (1.0.0)
description:
entry point: (index.js)
test command:
git repository:
keywords:
author:
license: (ISC)
About to write to /home/user/test/package.json:

{
  "name": "test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}


Is this ok? (yes)
```


