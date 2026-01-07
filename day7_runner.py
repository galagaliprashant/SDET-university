from api_framework.api_client import APIClient

client = APIClient("https://dummyjson.com")

import json

print("--- TEST 1: GET ---")
# DummyJSON has a user with ID 1
resp = client.get_user(1)
print(f"Status: {resp.status_code}")
try:
    print("Response Body:")
    print(json.dumps(resp.json(), indent=4))
except json.JSONDecodeError:
    print(f"Failed to decode JSON. Raw Text: {resp.text}")

print("\n--- TEST 2: POST ---")
# DummyJSON CREATE might fail with the current APIClient structure (which uses /users), 
# but let's try it. DummyJSON expects /users/add for creation, 
# so we might see a 404, but at least it should be JSON!
resp = client.create_user("SDET_Candidate", "Lead")
print(f"Status: {resp.status_code}")
try:
    print("Response Body:")
    print(json.dumps(resp.json(), indent=4))
except json.JSONDecodeError:
    print(f"Failed to decode JSON. Raw Text: {resp.text}")