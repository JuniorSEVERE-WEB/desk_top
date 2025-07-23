from exceptions import division

import pytest 

def test_division():
    assert division(3, 1) == 3

def test_division_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(3, 0)
         