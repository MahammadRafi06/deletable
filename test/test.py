import sys
import os

# Add the parent directory of 'utils' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code ==200
    assert response.data==b"Hello world!"