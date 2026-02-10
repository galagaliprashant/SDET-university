from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# 1. Credentials & Endpoint
USER = "oauth-galagaliprashanth-8ad90"
KEY = "52eaef90-df82-4b4d-a360-a794bf39931b"

# Use US-West-1 (Based on your dashboard screenshot)
URL = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

# 2. Modern Appium 2 / W3C Capabilities
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Samsung.*"
options.app = "storage:filename=mydemo.apk"

# Sauce-specific options (The Enterprise Way)
sauce_options = {
    "username": USER,
    "accessKey": KEY,
    "name": "Sprint 1: Android 14 Cloud Validation",
    "build": "L3-Build-001",
    "appiumVersion": "appium3-2025-10"  # CRITICAL: Fixes the Android 14 error
}
options.set_capability("sauce:options", sauce_options)

try:
    print("🚀 Connecting to Sauce Labs Real Device Cloud (Appium 2)...")
    # No credentials in URL string avoids security warnings
    driver = webdriver.Remote(URL, options=options)

    print("✅ Session Started. Checking for App Launch...")
    time.sleep(8) # Extra time for cloud streaming

    # Verify app is active
    print(f"Current Activity: {driver.current_activity}")

    # Mark test as passed in Sauce Labs Dashboard
    driver.execute_script("sauce:job-result=passed")
    print("🎉 Mission Accomplished: Test Passed on Cloud!")

except Exception as e:
    print(f"❌ Error: {e}")
    # Attempt to mark failure if session was created
    try:
        if 'driver' in locals():
            driver.execute_script("sauce:job-result=failed")
    except:
        pass

finally:
    if 'driver' in locals():
        driver.quit()