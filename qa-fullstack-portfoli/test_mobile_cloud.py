import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options


class TestMobileAutomation:
    import time

    @pytest.fixture
    def driver(self):
        # 1. Setup Capabilities
        USER = "oauth-galagaliprashanth-8ad90"
        KEY = "52eaef90-df82-4b4d-a360-a794bf39931b"
        URL = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "Samsung.*"
        options.app = "storage:filename=mydemo.apk"

        sauce_options = {
            "username": USER,
            "accessKey": KEY,
            "name": "L3 Portfolio: HTML Reporting Test",
            "build": "Build-HTML-001",
            "appiumVersion": "appium3-2025-10"
        }
        options.set_capability("sauce:options", sauce_options)

        # 2. Initialize Driver
        driver = webdriver.Remote(URL, options=options)
        yield driver

        # 3. Teardown
        driver.quit()

    def test_app_launch_and_activity(self, driver):
        """Verify the app launches and reaches the MainActivity"""
        print("🚀 Starting Cloud Test...")
        time.sleep(8)

        # Capture screenshot for the report
        driver.save_screenshot('report_screenshot.png')

        activity = driver.current_activity
        assert ".view.activities.MainActivity" in activity
        driver.execute_script("sauce:job-result=passed")

        def test_verify_main_activity(driver):
            """Scenario: Verify the app successfully launches to the Home Screen"""
            print("Step 1: Waiting for app sync...")
            time.sleep(8)

            activity = driver.current_activity
            assert ".view.activities.MainActivity" in activity

            driver.execute_script("sauce:job-result=passed")
            print("✅ Verified: Main Activity is active.")

        def test_app_package_check(driver):
            """Scenario: Verify the correct app package is installed"""
            print("Step 1: Checking package name...")
            package = driver.current_package
            assert "com.saucelabs.mydemoapp" in package.lower()

            driver.execute_script("sauce:job-result=passed")
            print(f"✅ Verified: Package {package} is correct.")