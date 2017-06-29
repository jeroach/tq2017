const assert = require('assert');
const code = require('../scripts/code');

describe('Test that the function returns correct value', function () {
    it('should return 5', function () {
        var expected_result = code.returnFive();
        assert.equal(5, expected_result);
    });
});
