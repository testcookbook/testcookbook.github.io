---
layout: default
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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.css"></link>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine-html.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/boot.js"></script>
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

View and example of it running [here](/book/javascript/jasmine/jasmine.html)