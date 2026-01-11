from api_framework.api_client import APIClient
from api_framework.schemas import user_schema
from jsonschema import validate, ValidationError

client = APIClient("https://reqres.in/api")

print("\n--- TEST 1: GET User + Schema Validation ---")
response = client.get_user(2)

# 1. Check Status (Basic)
if response.status_code == 200:
    print("✅ Status 200 OK")

    # 2. Check Data Structure (Advanced)
    try:
        json_data = response.json()
        validate(instance=json_data, schema=user_schema)
        print("✅ Schema Validation Passed (Data format is correct)")
    except ValidationError as e:
        print(f"❌ Schema Validation FAILED: {e.message}")
else:
    print(f"❌ HTTP Fail: {response.status_code}")