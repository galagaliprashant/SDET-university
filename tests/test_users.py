import pytest
from api_framework.schemas import user_schema
from jsonschema import validate

# Note: We do NOT import APIClient here anymore!
# We just ask for 'api_client' in the brackets.

def test_get_valid_user(api_client):
    """Test fetching a user using the fixture."""
    response = api_client.get_user(1)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "firstName" in data
    assert "email" in data
    assert data["id"] == 1

def test_create_user(api_client):
    """
    Test creating a user using the fixture.
    NOTE: This test is EXPECTED TO FAIL because DummyJSON returns 404 for this endpoint.
    """
    # DummyJSON returns 404 on POST /users usually
    response = api_client.create_user("Fixture_Bot", "Tester")
    
    # Intentionally asserting 201 to make the test FAIL (since it gets 404)
    assert response.status_code == 201, f"Expected 201 Created, but got {response.status_code}"

def test_user_not_found(api_client):
    """Test using fixture for negative testing."""
    response = api_client.get_user(99999)
    assert response.status_code == 404