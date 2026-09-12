# Selenium E-Commerce Automation Framework

## Project Overview

This project is a Selenium Python automation framework developed for the Capstone Assignment.

The framework automates key functionalities of the TutorialsNinja Demo e-commerce website using Selenium WebDriver and PyTest.

The framework follows the Page Object Model (POM) design pattern and includes reusable utilities for configuration management, CSV test data, logging, screenshots, and HTML reporting.

---

## Application Under Test

**Website:** TutorialsNinja Demo

**URL:** https://tutorialsninja.com/demo/

---

## Technologies Used

- Python
- Selenium WebDriver
- PyTest
- PyTest HTML
- Page Object Model (POM)
- CSV Test Data
- Configuration Management
- Python Logging

---

## Framework Features

The framework provides:

- Selenium WebDriver automation
- PyTest test execution
- Page Object Model
- Configuration management using `config.ini`
- CSV-based test data
- Explicit waits
- Implicit waits
- Automatic screenshots on test failure
- Logging
- HTML test reporting
- Reusable utility classes
- Automatic test discovery
- Clean project structure

---

## Project Structure

```text
Selenium_Ecommerce_Framework/
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
├── requirements.txt
│
├── base/
│   ├── __init__.py
│   └── base_test.py
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── product_search_page.py
│
├── reports/
│   ├── automation.log
│   └── test_report.html
│
├── screenshots/
│
├── test_data/
│   └── login_data.csv
│
├── tests/
│   ├── __init__.py
│   ├── test_browser.py
│   ├── test_login.py
│   └── test_product_search.py
│
├── utilities/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── logger.py
│   └── screenshot.py
│
└── venv/