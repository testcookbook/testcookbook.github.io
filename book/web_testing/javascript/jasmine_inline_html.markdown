---
layout: default
title:  "Jasmine tests inline with HTML"
description: "Inline HTML Jasmine tests"
---

# Jasmine Tests inline with HTML

Sometimes it can be nice to run tests within a browser.  You might could use it
to present a point or to validate how something works.  Whatever the case might
be Jasmine offers a simple way to run some tests within your browser.

To start off we need to include some external resources.  You can get these
files from either the NPM registry or you could link to the files on a CDN.

```html
<html>
<head>
  //within head tags
  <link href="jasmine.css" rel="stylesheet" type="text/css" />
  <script src="jasmine.min.js"></script>
  <script src="jasmine-html.min.js"></script>
  <script src="boot.min.js"></script>
</head>
```

Now that we have all of our dependencies lets create a new function that adds
2 numbers and see if the output is correct.

```html
  <body>
    <script>
      function adder(x, y) {
        return x + y;
      }


      describe('adder function', function () {
        it('2 + 2 should equal 4', function () {
          expect(adder(2,2)).toBe(4);
        })
      });
    </script>
  </body>
```

[http://www.testcookbook.com/book/web_testing/javascript/jasmine_inline_html.html](/book/web_testing/javascript/jasmine_inline_html.html)
