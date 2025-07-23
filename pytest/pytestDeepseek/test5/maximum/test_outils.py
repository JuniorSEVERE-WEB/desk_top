from outils import maximum
import pytest 

def test_maximum():
    assert maximum(5,3) == 5
    assert maximum(-1, -5) == -1 
