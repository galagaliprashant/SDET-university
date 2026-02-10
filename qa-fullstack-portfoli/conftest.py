import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver(request):
    # 1. Enterprise Credentials
    USER = "oauth-galagaliprashanth-8ad90"
    KEY = "52eaef90-df82-4b4d-a360-a794bf39931b"
    URL = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

    # 2. Advanced W3C Capabilities
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Samsung.*"
    options.app = "storage:filename=mydemo.apk"

    sauce_options = {
        "username": USER,
        "accessKey": KEY,
        "name": request.node.name,  # Automatically names the test in Sauce Labs
        "build": "L3-SDET-Sprint-1",
        "appiumVersion": "appium3-2025-10"
    }
    options.set_capability("sauce:options", sauce_options)

    # 3. Startup
    print(f"🚀 Initializing Cloud Driver for: {request.node.name}")
    driver = webdriver.Remote(URL, options=options)

    yield driver  # This provides the driver to your test functions

    # 4. Global Teardown
    print("🧹 Cleaning up session...")
    driver.quit()