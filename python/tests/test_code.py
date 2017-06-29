import pytest
from scripts import code


def test_return_5():
    expected_result = code.return_5()
    assert 5 == expected_result
