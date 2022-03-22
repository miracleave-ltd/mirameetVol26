import sqlite3
import pytest
 
def get_connection():
    con = sqlite3.connect('db.sqlite3')
    return con
 
@pytest.fixture
def cursor():
    with get_connection() as con:
        cur = con.cursor()
        print("\n" + "START TEST")
        yield cur
        print("\n" + "END TEST")
        con.rollback()