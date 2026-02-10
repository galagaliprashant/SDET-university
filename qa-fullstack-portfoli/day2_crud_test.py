import requests

# --- CONFIGURATION ---
BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}


# 1. HELPER: Get Auth Token (We need this to DELETE later)
def get_token():
    auth_data = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", json=auth_data, headers=HEADERS)
    return response.json()["token"]


# 2. STEP 1: CREATE a Booking
def create_booking():
    payload = {
        "firstname": "Prashanth",
        "lastname": "Sdet",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-05"},
        "additionalneeds": "Super Fast Wifi"
    }
    print("🚀 Creating Booking...")
    response = requests.post(f"{BASE_URL}/booking", json=payload, headers=HEADERS)

    if response.status_code == 200:
        booking_id = response.json()["bookingid"]
        print(f"✅ Created! ID: {booking_id}")
        return booking_id
    else:
        print(f"❌ Creation Failed: {response.status_code}")
        return None


# 3. STEP 2: VERIFY the Booking (Read)
def get_booking(booking_id):
    print(f"🔍 Verifying Booking ID: {booking_id}...")
    response = requests.get(f"{BASE_URL}/booking/{booking_id}", headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        if data["firstname"] == "Prashanth":
            print("✅ Data Match: First Name is correct.")
        else:
            print("❌ Data Mismatch!")
    else:
        print("❌ Could not find booking!")


# 4. STEP 3: DELETE the Booking (Cleanup)
def delete_booking(booking_id, token):
    print(f"🗑️ Deleting Booking ID: {booking_id}...")
    # Note: Delete requires a 'Cookie' header with the token
    cookie_header = {"Cookie": f"token={token}"}
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=cookie_header)

    if response.status_code == 201:
        print("✅ Deleted Successfully!")
    else:
        print(f"❌ Delete Failed: {response.status_code}")


# --- EXECUTION FLOW ---
if __name__ == "__main__":
    # A. Get Token
    my_token = get_token()

    # B. Run the Chain
    my_id = create_booking()
    if my_id:
        get_booking(my_id)
        delete_booking(my_id, my_token)