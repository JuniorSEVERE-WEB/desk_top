import pytest 
from string_utils import reverse_string

def test_reverse_normal():
    assert reverse_string("hello") == "olleh"

def test_reverse_error():
    with pytest.raises(ValueError):
        reverse_string(123)
    