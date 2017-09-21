import os
import pytest


@pytest.fixture
def setup_file():
    f = open('test_file.txt', 'a+')
    f.write('Some text')
    f.seek(0)  # needed for Windows specific bug

    yield f

    print('Closing and deleting file')
    f.close()
    os.remove('test_file.txt')


def test_1_with_setup_and_teardown(setup_file):
    text = setup_file.read()
    assert text == 'Some text'

    setup_file.write(' More text')
    setup_file.seek(0)  # needed for Windows specific bug
    new_text = setup_file.read()
    assert new_text == 'Some text More text'


def test_2_with_setup_and_teardown(setup_file):
    text = setup_file.read()
    assert text == 'Some text'

    setup_file.write(' Different text')
    setup_file.seek(0)  # needed for Windows specific bug
    new_text = setup_file.read()
    assert new_text == 'Some text Different text'
