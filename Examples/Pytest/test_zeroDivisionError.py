import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
        1 / 0

def test_zero_divisionFail():
    with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
        1 / 2