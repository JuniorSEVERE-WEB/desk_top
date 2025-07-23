# 1. Assertions simples

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 10 - 4 == 6

# 2. Tester des exceptions
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error():
    with pytest.raises(ValueError):
        int('abc')

# 3. Paramétrisation
import pytest

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (10, 5, 15)
])
def test_param_add(a, b, result):
    assert a + b == result

@pytest.mark.parametrize("x,y", [
    (4, 2),
    (9, 3)
])
def test_param_divisible(x, y):
    assert x % y == 0

# 4. Fixtures
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3]

def test_list_length(sample_list):
    assert len(sample_list) == 3

@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}

def test_user_name(user):
    assert user["name"] == "Alice"

# 5. Organisation avec classes
class TestMath:
    def test_mul(self):
        assert 3 * 4 == 12
    def test_div(self):
        assert 8 / 2 == 4

class TestString:
    def test_upper(self):
        assert "abc".upper() == "ABC"
    def test_isdigit(self):
        assert not "abc".isdigit()
