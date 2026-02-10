from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- SETUP ---
# 1. Initialize the Chrome Browser
# (ChromeDriverManager automatically installs the right driver version for you)
print("🚀 Launching Browser...")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 2. Open the Target Website
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

try:
    # --- STEP 1: LOGIN ---
    print("🔑 Logging in...")

    # Find elements by ID (The most stable locator strategy)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verification: Did we land on the products page?
    # We check if the "Products" title is visible
    header = driver.find_element(By.CLASS_NAME, "title").text
    if header == "Products":
        print("✅ Login Successful!")
    else:
        print("❌ Login Failed!")
        exit()

    # --- STEP 2: ADD TO CART ---
    print("🎒 Adding Backpack to Cart...")

    # We use "ID" again because developers gave this button a unique ID
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # --- STEP 3: VERIFY CART STATE ---
    # Check if the little red badge says "1"
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    if cart_badge == "1":
        print("✅ Success: Cart shows 1 item.")
    else:
        print(f"❌ Failure: Cart shows {cart_badge}")

    time.sleep(10)  # Pausing so you can see the result before it closes

except Exception as e:
    print(f"❌ Something went wrong: {e}")

finally:
    # --- TEARDOWN ---
    # Always close the browser, even if the test fails
    print("👋 Closing Browser...")
    driver.quit()