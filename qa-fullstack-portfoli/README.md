# Enterprise Cloud-Native Mobile Automation Framework 🚀

## Overview
This repository contains a professional-grade mobile automation framework engineered for high-scale, cross-platform execution. Developed during an intensive SDET sprint, the framework is optimized for modern mobile environments (Android 14+) and handles the complexities of cloud-based real device execution.

## 🏗️ Architectural Design
Unlike standard linear scripts, this framework implements a **Modular Configuration Pattern**:

- **Global Driver Management**: Leverages a centralized `conftest.py` engine to manage the Appium driver lifecycle across multiple test suites.

- **W3C Protocol Compliance**: Fully migrated to Appium 3.x standards to ensure compatibility with modern mobile security and OS architectures.

- **Cloud-Native Integration**: Engineered specifically for Sauce Labs Real Device Cloud (RDC), allowing for high-fidelity testing on physical hardware without the flakiness of local emulators.

## 🛠️ Technology Stack
- **Language**: Python 3.9+
- **Test Runner**: Pytest (Modular Fixtures)
- **Automation Engine**: Appium 3.x
- **Cloud Backend**: Sauce Labs Real Device Cloud
- **Reporting**: Allure Reporting & Pytest-HTML

## 📊 Reporting & Observability
The framework prioritizes executive-level visibility:

- **Allure Dashboard**: Provides interactive graphs, trend analysis, and step-by-step execution logs.
- **Evidence Collection**: Automatically captures screenshots and embeds them into the report upon failure for rapid debugging.

## 🚀 CI/CD Readiness
The framework is designed for Continuous Integration:

- **Decoupled Logic**: Environment credentials and capabilities are separated from test logic to allow for seamless injection via GitHub Actions secrets.
- **Parallel Execution**: Ready for pytest-xdist integration to run tests concurrently across multiple cloud devices.

## 🏁 Quick Start

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Execute Tests:
```bash
pytest qa-fullstack-portfoli/test_mobile_cloud.py --alluredir=allure-results
```

### Generate Report:
```bash
allure serve allure-results
```

## 📁 Project Structure
```
qa-fullstack-portfoli/
├── conftest.py                 # Global fixtures and driver management
├── day1_api_test.py           # RESTful API testing examples
├── day2_crud_test.py          # Database CRUD operations
├── day3_web_shop.py           # E-commerce automation
├── day4_web_checkout.py       # Checkout flow testing
├── day5_mobile_automation.py  # Mobile app testing
├── test_mobile_cloud.py       # Cloud-based mobile testing
└── README.md                  # This file
```

## 🎯 Key Features
- ✅ Cross-platform mobile automation (Android/iOS)
- ✅ Cloud device integration (Sauce Labs RDC)
- ✅ Comprehensive test reporting with Allure
- ✅ Modular and maintainable architecture
- ✅ CI/CD pipeline ready
- ✅ Screenshot capture on failure
- ✅ W3C WebDriver protocol compliant

## 📈 Test Execution Results
View the latest test execution reports in the `allure-results/` directory or generate an interactive dashboard using the commands above.

---

**Developed by**: Prashanth Galagali  
**Framework Type**: Enterprise Mobile Automation  
**Status**: Production Ready ✅
