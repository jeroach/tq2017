const assert = require('assert');

function returnFive() {
    return 5;
}

describe('Test that the function returns correct value', function () {
    it('should return 5', function () {
        const result = returnFive();
        assert.equal(5, result);
    });
});
