import os
import pytest

value = 5


@pytest.fixture(autouse=True)
def setup_and_teardown():
    value = 7
    yield
    value = 5


def return_value():
    return value


def test_setup_and_teardown(setup_and_teardown):
    expected_result = return_value()
    assert 5 == expected_result
