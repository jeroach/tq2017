import pytest
from unittest import mock
from scripts import code


def test_return_5():
    expected_result = code.return_5()
    assert 5 == expected_result


@pytest.mark.parametrize('listA,listB,expected_result', [
  (['A', 'B'], ['C', 'D'], ['A', 'B', 'C', 'D']),
  (['A', 'A'], ['A', 'B'], ['A', 'B']),
  ([], ['C'], ['C']),
  ([], [], [])
])
def test_merge_2_lists(listA, listB, expected_result):
    result = code.merge_2_lists(listA, listB)
    assert result == expected_result


@mock.patch('os.walk')
def test_get_filenames_in_directory(mockwalk):
    folders = ['folder1', 'folder2']
    files = ['a.txt', 'b.txt', 'c.png']
    mockwalk.return_value = [('/root', folders, files)]

    result = code.get_filenames_in_directory('path')
    assert len(result) == 3
    assert result == files
