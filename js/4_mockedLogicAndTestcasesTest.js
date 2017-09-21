const fs = require('fs');
const sinon = require('sinon');
const assert = require('assert');

function getFilenamesInDirectory(directory) {
    let fileNames = [];
    fs.readdir(directory, (err, files) => {
        files.forEach(file => {
            fileNames.push(file);
        });
    });
    return fileNames;
}

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
// http://sinonjs.org/releases/v3.3.0/stubs/
describe('Test that testcases work in parallel with stubbed logic', function () {
    const tests = [
        {files: ['a.txt', 'b.txt', 'c.png']},
        {files: ['a.txt', 'c.png']},
        {files: []},
        {files: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}
    ];

    tests.forEach(function(test) {
        it('stub should return list of files containing ' + test.files, function () {
            let fsStub = sinon.stub(fs, 'readdir').callsFake(function(path, callback) {
                callback(null, test.files);
            });

            const result = getFilenamesInDirectory('path');
            assert.equal(result.length, test.files.length);
            assert.deepEqual(result, test.files); // structual equality (checks that operands are equivalent)

            fsStub.restore();
        });
    });
});
