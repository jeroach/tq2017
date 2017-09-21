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

// https://mochajs.org/#hooks
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
    it('mock should be called again', function () {
        const expect = fsMock.expects('readdir').once().withArgs('path');
        const result = getFilenamesInDirectory('path');
        expect.verify();
    });
    it('mock should be called with a different path', function () {
        const expect = fsMock.expects('readdir').once().withArgs('anotherPath');
        const result = getFilenamesInDirectory('anotherPath');
        expect.verify();
    });
});
