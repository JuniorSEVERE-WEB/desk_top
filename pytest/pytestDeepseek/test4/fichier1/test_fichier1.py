import pytest 

from fichier1 import add 

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (0, 0, 0),
])

def test_add(a, b, expected):
    assert add(a, b) == expected