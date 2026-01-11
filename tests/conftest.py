import pytest
from api_framework.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    """
    This fixture initializes the API Client once for the entire test session.
    It acts like a 'Singleton' - providing the tool to any test that needs it.
    """
    print("\n   ⚡ [Setup] Connecting to API...")
    # Using DummyJSON to ensure tests pass (ReqRes returns 403)
    client = APIClient("https://dummyjson.com")
    
    yield client  # This passes the object to the test
    
    print("\n   🧹 [Teardown] Closing connection (Simulated)...")