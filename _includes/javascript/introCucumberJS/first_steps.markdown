```javascript
var assert = require('assert');
module.exports = function () {
    var a, b, t;
    this.Given(/^numbers (\d+) and (\d+)$/, function (arg1, arg2) {
        a = Number(arg1);
        b = Number(arg2);
    });

    this.When(/^they are added together$/, function () {
        t = a + b;
    });

    this.Then(/^the total should be (\d+)$/, function (arg1) {
        assert.equal(t, 7);
    });
}
```