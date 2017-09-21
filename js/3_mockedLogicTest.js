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

// http://sinonjs.org/releases/v3.3.0/mocks/
describe('Test that the function is mocked correctly', function () {
    it('mock should be called', function () {
        let fsMock = sinon.mock(fs);

        const expect = fsMock.expects('readdir').once().withArgs('path');
        const result = getFilenamesInDirectory('path');
        expect.verify();

        fsMock.restore();
    });
});

// http://sinonjs.org/releases/v3.3.0/stubs/
describe('Test that the function is stubbed correctly', function () {
    it('stub should return expected value', function () {
        const files = ['a.txt', 'b.txt', 'c.png'];
        let fsStub = sinon.stub(fs, 'readdir').callsFake(function(path, callback) {
            callback(null, files);
        });

        const result = getFilenamesInDirectory('path');
        assert.deepEqual(result, files); // structual equality (checks that operands are equivalent)

        fsStub.restore();
    });
});
