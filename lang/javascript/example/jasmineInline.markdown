---
layout: jasmine
title:  "Jasmine tests inline with HTML"
---

  {% highlight HTML %}
  <html>
  <head>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/jasmine/2.5.2/jasmine.css" rel="stylesheet" type="text/css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/2.5.2/jasmine.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/2.5.2/jasmine-html.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/2.5.2/boot.min.js"></script>
  </head>
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
  <body>
  </html>
  {% endhighlight %}

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
