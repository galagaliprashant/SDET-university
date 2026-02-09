import requests
import json

class APIClient:
    """A reusable client for interacting with REST APIs."""
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self, user_id):
        endpoint = f"{self.base_url}/users/{user_id}"
        print(f"GET Request -> {endpoint}")
        return requests.get(endpoint)

    def create_user(self, name, job):
        endpoint = f"{self.base_url}/users"
        payload = {"name": name, "job": job}
        print(f"POST Request -> {endpoint} | Payload: {payload}")
        return requests.post(endpoint, json=payload)

if __name__ == "__main__":
    # Ensures this block runs only when the file is executed directly, not when imported
    
    # Create an instance of APIClient with the base URL
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    # Call get_user method to fetch user with ID 2 (sends GET request)
    response_get = client.get_user(2)
    
    # Call create_user method to add a new user (sends POST request)
    response_post = client.create_user("Prashanth", "SDET")
    
    # Print the status code and JSON response body for the GET request
    print(f"Status Code: {response_get.status_code}")
    print("Response Body:")
    print(json.dumps(response_get.json(), indent=4))
    
    # Print the status code and JSON response body for the POST request
    print(f"Status Code: {response_post.status_code}")
    print("Response Body:")
    print(json.dumps(response_post.json(), indent=4))

    print("\n" + "="*50 + "\n")
    print("--- Creating Second Instance (GoRest API) ---")
    # Second instance pointing to GoRest (Public API)
    client_gorest = APIClient("https://gorest.co.in/public/v2")
    response_gorest = client_gorest.get_user(2) # GoRest usually has users, checking ID 2
    print(f"GoRest User Status: {response_gorest.status_code}")
    # GoRest might return 404 if user 2 doesn't exist, but it returns JSON. 
    # If it fails, we handle it by checking status.
    if response_gorest.status_code == 200:
        print(f"GoRest User Body: {json.dumps(response_gorest.json(), indent=4)}")
    else:
        print(f"GoRest User Body: {response_gorest.text}")

    print("\n" + "="*50 + "\n")
    print("--- Creating Third Instance (DummyJSON) ---")
    # Third instance pointing to DummyJSON
    client_dummy = APIClient("https://dummyjson.com")
    # DummyJSON uses /users/{id} structure as well
    response_dummy = client_dummy.get_user(1) 
    print(f"DummyJSON User Status: {response_dummy.status_code}")
    print(f"DummyJSON User Body: {json.dumps(response_dummy.json(), indent=4)}")
