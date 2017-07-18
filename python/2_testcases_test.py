import pytest


def merge_2_lists(listA, listB):
    mergedList = []
    mergedList.extend(a for a in listA if a not in mergedList)
    mergedList.extend(b for b in listB if b not in mergedList)
    return mergedList


@pytest.mark.parametrize('listA,listB,expected_result', [
  (['A', 'B'], ['C', 'D'], ['A', 'B', 'C', 'D']),
  (['A', 'A'], ['A', 'B'], ['A', 'B']),
  ([], ['C'], ['C']),
  ([], [], [])
])
def test_with_cases(listA, listB, expected_result):
    result = merge_2_lists(listA, listB)
    assert result == expected_result
