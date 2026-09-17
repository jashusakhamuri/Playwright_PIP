# Playwright Automation Framework

## Overview

A Python-based UI automation framework built using Playwright and Pytest for testing the SauceDemo web application.

The framework follows the Page Object Model (POM) and separates locators, page actions, test cases, configuration, and test data.

The project currently contains **21 automated test cases** covering Login, Products, Cart, and Checkout.

## Application Under Test

**SauceDemo**  
https://www.saucedemo.com/

## Tech Stack

- Python
- Playwright
- Pytest
- Pytest-Playwright
- Pytest-HTML
- Pytest-XDist
- PyYAML
- XPath
- VS Code

## Framework Features

- Page Object Model
- Separate locator files
- XPath locators
- YAML-based test data
- YAML-based configuration
- Pytest fixtures
- Logging
- Automatic failure screenshots
- HTML test reports
- Parallel test execution
- 21 automated test cases

## Project Structure

```text
Playwright-automation/
│
├── config/
│   └── config.yaml
│
├── locators/
│   ├── login_locators.py
│   ├── products_locators.py
│   ├── cart_locators.py
│   └── checkout_locators.py
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── test_data/
│   └── test_data.yaml
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   ├── config_reader.py
│   ├── test_data_reader.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

### 1. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 2. Activate the Virtual Environment

```powershell
.venv\Scripts\activate
```

### 3. Install Project Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```powershell
python -m playwright install
```

## Commands Used to Run the Project

### Check Pytest Version

```powershell
python -m pytest --version
```

### Run All Test Cases

```powershell
python -m pytest
```

This runs all **21 automated test cases**.

### Run Login Tests

```powershell
python -m pytest tests/test_login.py
```

### Run Products Tests

```powershell
python -m pytest tests/test_products.py
```

### Run Cart Tests

```powershell
python -m pytest tests/test_cart.py
```

### Run Checkout Tests

```powershell
python -m pytest tests/test_checkout.py
```

### Run Tests in Parallel

```powershell
python -m pytest -n 4
```

The `-n 4` option runs the tests using four workers.

## Test Results

The framework contains **21 automated test cases**:

- Login: 5
- Products: 6
- Cart: 3
- Checkout: 7

All 21 test cases were executed successfully.

## Reports

### HTML Report

The HTML test report is generated at:

```text
reports/report.html
```

### Automation Logs

The automation log is generated at:

```text
reports/automation.log
```

### Failure Screenshots

When a test fails, a screenshot is automatically captured and saved in:

```text
screenshots/
```

## Test Coverage

### Login

- Valid login
- Invalid login
- Empty username
- Empty password
- Locked-out user

### Products

- Products page validation
- Add product to cart
- Remove product from cart
- Open product details
- Sort products A-Z
- Sort products by price

### Cart

- Open cart
- Verify product appears in cart
- Remove product from cart

### Checkout

- Open checkout
- Valid checkout information
- First name validation
- Last name validation
- Postal code validation
- Verify product in checkout overview
- Complete checkout

## Future Improvements

- Pytest markers
- Cross-browser execution
- GitHub Actions CI/CD
- Additional test scenarios
- API automation

## Author

**Kalava Yamini Krishna**

B.Tech - Computer Science and Engineering