const assert = require('assert');

function merge2Lists(listA, listB) {
    const withDuplicates = listA.concat(listB);
    const mergedList = Array.from(new Set(withDuplicates));
    return mergedList;
}

describe('Test that the lists are correctly merged', function () {
    const tests = [
        {listA: ['A', 'B'], listB: ['C', 'D'], expected: ['A', 'B', 'C', 'D']},
        {listA: ['A', 'A'], listB: ['A', 'B'], expected: ['A', 'B']},
        {listA: [], listB: ['C'], expected: ['C']},
        {listA: [], listB: [], expected: []}
    ];

    tests.forEach(function(test) {
        it('should return list containing ' + test.expected, function () {
            const result = merge2Lists(test.listA, test.listB);
            assert.deepEqual(result, test.expected);
        });
    });
});
