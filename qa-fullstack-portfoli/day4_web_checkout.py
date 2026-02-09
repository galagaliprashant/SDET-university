from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- SETUP ---
options = webdriver.ChromeOptions()
# options.add_argument("--headless") # Uncomment to run without opening a window (Pro Mode)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    print("🚀 Starting E2E Checkout Flow...")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # 1. LOGIN (Fast)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. ADD TO CART
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 3. GO TO CART
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. CHECKOUT START
    # Pro Tip: Always check if the button is clickable before clicking
    wait = WebDriverWait(driver, 5)
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # 5. FILL FORM (The "Data Entry" phase)
    print("📝 Filling Shipping Info...")
    driver.find_element(By.ID, "first-name").send_keys("Prashanth")
    driver.find_element(By.ID, "last-name").send_keys("SDET")
    driver.find_element(By.ID, "postal-code").send_keys("560010")
    driver.find_element(By.ID, "continue").click()

    # 6. FINAL VALIDATION (The Money Shot)
    # We need to verify the Total Price is correct
    total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    print(f"💰 Invoice Total: {total_text}")

    finish_btn = driver.find_element(By.ID, "finish")
    finish_btn.click()

    # 7. SUCCESS MESSAGE
    success_header = driver.find_element(By.CLASS_NAME, "complete-header").text
    if "Thank you" in success_header:
        print("✅ ORDER PLACED SUCCESSFULLY!")
    else:
        print("❌ Order Failed.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    time.sleep(3)
    driver.quit()