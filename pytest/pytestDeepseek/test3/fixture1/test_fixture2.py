import pytest 

@pytest.fixture 
def donnees():
    return {"nom": "Junior", "age":31}

def test_age(donnees):
    assert donnees["age"] == 31