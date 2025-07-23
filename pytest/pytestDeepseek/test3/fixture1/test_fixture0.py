from .fixture0 import Database
import pytest

@pytest.fixture 
def database():
    db = Database()
    yield db 
    db.close()

def test_query(database):
    assert database.query("SELECT 1")
