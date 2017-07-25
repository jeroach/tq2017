const fs = require('fs');
const sinon = require('sinon');

function getFilenamesInDirectory(directory) {
    fileNames = [];
    fs.readdir(directory, (err, files) => {
        files.forEach(file => {
            fileNames.push(file);
        });
    });
    return fileNames;
}

describe('Test that the function is mocked correctly', function () {
    let mock;
    before(function (done) {
        mock = sinon.mock(fs);
        done();
    });
    after(function (done) {
        mock.restore();
        done();
    });

    it('mock should be called', function () {
        const expect = mock.expects('readdir').once().withArgs('path');
        var result = getFilenamesInDirectory('path');
        expect.verify();
    });
});
