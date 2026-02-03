# Enterprise ERP Automation & Security Testing
**Path:** `Cybersecurity-Projects / erp_automation_suite.py`

## Project Overview
This project demonstrates the automation of a complex financial workflow within an Enterprise Resource Planning (ERP) system. Originally developed during my tenure in Quality Assurance, I have **sanitized and refactored** this suite to demonstrate a security-first approach to automation.

The script automates the end-to-end lifecycle of Accounts Payable, from secure authentication to batch payment processing and check generation.

## Technical Skills Demonstrated
* **Browser Automation:** Utilizing Selenium WebDriver for complex UI interactions (ExtJS framework).
* **Security Sanitization:** Implementation of data masking and removal of PII (Personally Identifiable Information) and proprietary corporate metadata.
* **Anti-Bot Simulation:** Use of custom "human-like" typing functions to bypass basic heuristic detection.
* **Dynamic Data Handling:** Generating unique test artifacts (Invoice IDs/Dates) to ensure non-repudiation in testing.
* **Advanced Synchronization:** Managing asynchronous UI states using `WebDriverWait` and `Expected Conditions`.

## Security & Privacy Features
In transitioning this project to my public portfolio, I performed a **Security Audit** on the source code:
1.  **Credential Masking:** Replaced hardcoded administrative credentials with generic environment placeholders.
2.  **Path Scrubbing:** Removed all local file system paths (e.g., OneDrive/local screenshots) to prevent internal directory disclosure.
3.  **PII Removal:** All vendor names, GL accounts, and financial figures are now mocked "dummy" data.



## How it Works
The automation suite is broken down into three logical phases:
1.  **Authentication:** Secure login and session initialization.
2.  **AP Lifecycle:** Creation of Bills, Distribution of GL Accounts, and Note attachments.
3.  **Financial Processing:** Batch approval of paid bills and execution of the print-check workflow.

## Requirements
* Python 3.x
* Selenium
* Chrome WebDriver

---
*This project is part of my professional transition from Quality Assurance to Cybersecurity. It reflects my ability to handle complex enterprise systems while maintaining strict data privacy standards.*
