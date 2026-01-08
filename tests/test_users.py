import pytest
from api_framework.api_client import APIClient
from api_framework.schemas import user_schema
from jsonschema import validate

# 1. Setup (Fixture concept - we will learn more later)
# For now, we just create the client inside the test or as a global var
# 1. Setup (Fixture concept - we will learn more later)
# Switching to DummyJSON because ReqRes is blocking us (403)
client = APIClient("https://dummyjson.com")

def test_get_valid_user():
    """
    Verify that we can fetch a user.
    """
    print("   ---> Executing Test: Get Valid User")
    
    # Action
    response = client.get_user(1)
    
    # Assertions
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    
    data = response.json()
    # DummyJSON returns 'firstName', 'lastName', 'email' at the root level
    assert "firstName" in data
    assert "email" in data
    assert data["id"] == 1

def test_create_user():
    """
    Verify that creating a user returns 201 Created.
    NOTE: This test is EXPECTED TO FAIL because DummyJSON returns 404 for this endpoint.
    """
    print("   ---> Executing Test: Create User path")
    
    response = client.create_user("PyTest_Bot", "Automator")
    
    # We assert 201 to intentionally FAIL this test (got 404)
    assert response.status_code == 201, f"Expected 201 Created, but got {response.status_code}"

def test_user_not_found():
    """
    Negative Testing: Verify the API handles missing users correctly.
    """
    print("   ---> Executing Test: User Not Found")
    
    response = client.get_user(99999) # This user doesn't exist
    
    assert response.status_code == 404