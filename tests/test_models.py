import pytest
from models import add_item_db

def test_add_item(db):
    db.add_item_db("Roger","School","GoHome@gmail.com")

    
