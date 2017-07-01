---
layout: default
---
# Tiny Validator v4

### Setup

If you are running from NodeJS you can install via NPM.  There are applications like Postman which already include it for their scripting.

```
npm install tv4-node
```

### Simple Usage

```javascript
var tv4 = require("tv4-node").tv4;

var jsonData = {
    "name": 12345
}

var schema = {
    "properties": {
        "name": {
            "type": "number"
        }
    }
};

console.log(tv4.validate(jsonData, schema));
```

Basic usage for Tiny Validator is to simply validate your JSON data against a schema.  
