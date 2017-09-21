const assert = require('assert');

function returnFive() {
    return 5;
}

// https://nodejs.org/api/assert.html
describe('Test that the function returns correct value', function () {
    it('should return 5', function () {
        const result = returnFive();
        assert.equal(result, 5);
    });
});
