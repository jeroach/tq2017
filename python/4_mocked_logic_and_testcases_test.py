import os
import pytest
from unittest import mock


def get_filenames_in_directory(directory):
    fileNames = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            fileNames.append(name)
    return fileNames


# https://docs.pytest.org/en/latest/parametrize.html
# https://docs.python.org/3/library/unittest.mock.html
@mock.patch('os.walk')
@pytest.mark.parametrize('files,expected_count', [
  (['a.txt', 'b.txt', 'c.png'], 3),
  (['a.txt', 'c.png'], 2),
  ([], 0),
  (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 10)
])
def test_with_mocked_logic_and_test_cases(mockwalk, files, expected_count):
    folders = ['folder1', 'folder2']
    mockwalk.return_value = [('/root', folders, files)]

    result = get_filenames_in_directory('path')
    assert len(result) == expected_count
    assert result == files
    mockwalk.assert_called_once_with('path')
