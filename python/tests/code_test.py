import pytest
from unittest import mock
from scripts import code


def test_simple_assert():
    expected_result = code.return_5()
    assert 5 == expected_result


@pytest.mark.parametrize('listA,listB,expected_result', [
  (['A', 'B'], ['C', 'D'], ['A', 'B', 'C', 'D']),
  (['A', 'A'], ['A', 'B'], ['A', 'B']),
  ([], ['C'], ['C']),
  ([], [], [])
])
def test_with_cases(listA, listB, expected_result):
    result = code.merge_2_lists(listA, listB)
    assert result == expected_result


@mock.patch('os.walk')
def test_with_mocked_logic(mockwalk):
    folders = ['folder1', 'folder2']
    files = ['a.txt', 'b.txt', 'c.png']
    mockwalk.return_value = [('/root', folders, files)]

    result = code.get_filenames_in_directory('path')
    assert len(result) == 3
    assert result == files


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

    result = code.get_filenames_in_directory('path')
    assert len(result) == expected_count
    assert result == files
