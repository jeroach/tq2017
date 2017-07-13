import pytest
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
