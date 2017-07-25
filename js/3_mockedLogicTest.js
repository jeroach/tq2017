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

describe('Test that the function is mocked correctly', function () {
    let fsMock;
    before(function (done) {
        fsMock = sinon.mock(fs);
        done();
    });
    after(function (done) {
        fsMock.restore();
        done();
    });

    it('mock should be called', function () {
        const expect = fsMock.expects('readdir').once().withArgs('path');
        const result = getFilenamesInDirectory('path');
        expect.verify();
    });
});

describe('Test that the function is stubbed correctly', function () {
    const files = ['a.txt', 'b.txt', 'c.png'];
    let fsStub;
    before(function (done) {
        fsStub = sinon.stub(fs, 'readdir').callsFake(function(path, callback) {
            callback(null, files);
        });
        done();
    });
    after(function (done) {
        fsStub.restore();
        done();
    });

    it('stub should return expected value', function () {
        const result = getFilenamesInDirectory('path');
        assert.deepEqual(result, files); // structual equality (checks that operands are equivalent)
    });
});
