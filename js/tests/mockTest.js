const sinon = require('sinon');
const classToBeMocked = require('mockedClass');
const code = require('../scripts/code');

describe('Test that the function behaves correctly', function () {
    let mock;
    before(function (done) {
        mock = sinon.mock(classToBeMocked);
        done();
    });
    after(function (done) {
        mock.restore();
        done();
    });

    it('mock should be called', function () {
        const expect = mock.expects("methodName").once();
        // call method where mock is called
        expect.verify();
    });
});
