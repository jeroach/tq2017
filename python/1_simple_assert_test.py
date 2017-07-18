import pytest


def return_5():
    return 5


def test_simple_assert():
    expected_result = return_5()
    assert 5 == expected_result
