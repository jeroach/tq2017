import os
import pytest


# https://docs.pytest.org/en/latest/fixture.html
@pytest.fixture(scope='class')
def setup_file(request):
    f = open('test_file.txt', 'a+')
    f.write('Some text')
    f.seek(0)  # needed for Windows specific bug

    def teardown():
        print('Closing and deleting file')
        f.close()
        os.remove('test_file.txt')
    request.addfinalizer(teardown)
    return f


@pytest.mark.parametrize('updated_text,expected_result', [
  (' More text', 'Some text More text'),
  (' Different text', 'Some text Different text')
])
def test_with_setup_and_teardown(setup_file, updated_text, expected_result):
    text = setup_file.read()
    assert text == 'Some text'

    setup_file.write(updated_text)
    setup_file.seek(0)  # needed for Windows specific bug
    new_text = setup_file.read()
    assert new_text == expected_result
