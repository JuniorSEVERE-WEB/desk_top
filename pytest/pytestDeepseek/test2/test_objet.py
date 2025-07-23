import pytest



class Database:
    def query(self, sql):
        if sql == "SELECT 1":
            return 1
    def close(self):
        pass

@pytest.fixture 
def database():
    db = Database()
    yield db 
    db.close()

def test_query(database):
    assert database.query("SELECT 1") == 1    