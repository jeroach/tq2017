const assert = require('assert');

var returnFive = function() {
    return 5;
}

describe('Test that the function returns correct value', function () {
    it('should return 5', function () {
        var expected_result = returnFive();
        assert.equal(5, expected_result);
    });
});
