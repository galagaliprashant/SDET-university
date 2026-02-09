import requests

# 1. Define the Target
url = "https://restful-booker.herokuapp.com/auth"
headers = {"Content-Type": "application/json"}

# 2. The Payload (Data)
data = {
    "username": "admin",
    "password": "password123"
}

# 3. The Action (Hit the API)
print("🚀 Attempting to generate Token...")
response = requests.post(url, json=data, headers=headers)

# 4. The Validation (Did it work?)
if response.status_code == 200:
    token = response.json().get("token")
    print(f"✅ Success! Token generated: {token}")
else:
    print(f"❌ Failed! Status Code: {response.status_code}")