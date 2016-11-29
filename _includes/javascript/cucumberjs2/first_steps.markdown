```javascript
var chai = require('chai');
var assert = chai.assert;
var expect = chai.expect;
var should = chai.should();

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
        expect(t).to.equal(7);
        t.should.equal(7);
    });
}
```