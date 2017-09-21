import os
import pytest
from unittest import mock


def get_filenames_in_directory(directory):
    fileNames = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            fileNames.append(name)
    return fileNames


@mock.patch('os.walk')
def test_with_mocked_logic(mockwalk):
    folders = ['folder1', 'folder2']
    files = ['a.txt', 'b.txt', 'c.png']
    mockwalk.return_value = [('/root', folders, files)]

    result = get_filenames_in_directory('path')
    assert len(result) == 3
    assert result == files
    assert mockwalk.call_count == 1
