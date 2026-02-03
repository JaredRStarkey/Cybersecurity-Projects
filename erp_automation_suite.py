# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import random
import os

# Utility function to simulate human typing for stability and anti-bot measures
def type_like_human(element, text, delay=0.05):
    element.clear()
    for ch in str(text):
        element.send_keys(ch)
        time.sleep(delay)

# Initialize WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Step 1: Initialize Environment
# Using a generic local address for demonstration of ERP system automation
driver.get("http://localhost:8080") 
today_with_zeros = datetime.today().strftime('%m-%d-%Y')
driver.maximize_window()

# Step 2: Authentication Workflow
try:
    login_init = wait.until(EC.presence_of_element_located((By.ID, "login-init-button")))
    login_init.click()
    
    # Enter credentials (using generic placeholders for portfolio safety)
    username_field = driver.find_element(By.NAME, "USER_LOGIN_FIELD")
    username_field.send_keys("portfolio_admin")

    password_field = driver.find_element(By.NAME, "USER_PASSWORD_FIELD")
    password_field.send_keys("SecurityPass123!")

    login_submit = driver.find_element(By.XPATH, '//*[@data-qtip="Log into application"]')
    login_submit.click()
    print("✅ Authentication sequence completed.")
except TimeoutException:
    print("❌ Login page failed to load.")

# Step 3: Module Navigation (Accounts Payable)
time.sleep(5)
# Using JavaScript to trigger menu for complex UI frameworks
driver.execute_script("console.log('Opening Navigation Menu...');")

accounts_payable = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//span[text()='Accounts Payable']")
))
driver.execute_script("arguments[0].scrollIntoView(true);", accounts_payable)
actions = ActionChains(driver)
actions.move_to_element(accounts_payable).perform()

# Navigate to Bills
bills = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Bills']")))
bills.click()

# Step 4: Data Entry - Create New Bill
add_bills = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-qtip="Add new bill"]')))
add_bills.click()

# Select Vendor from Dropdown
vendors = driver.find_elements(By.XPATH, "//div[contains(@class, 'form-arrow-trigger')]")
if vendors:
    driver.execute_script("arguments[0].click();", vendors[0]) 

# Select first available vendor in bound list
vendor_item = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.list-item-selector")))
vendor_item[0].click()

# Step 5: Form Validation and Checkbox Toggling
amount_field = driver.find_element(By.NAME, "ENTRY_AMOUNT")
actions.double_click(amount_field).perform()
amount_field.send_keys(Keys.DELETE)
type_like_human(amount_field, "150.00")

# Generate unique test data for Invoice Number
invoice_num = f"INV-{random.randint(1000, 9999)}"
invoice_field = driver.find_element(By.NAME, "INVOICE_NUMBER")
invoice_field.send_keys(invoice_num)

# Toggle functional flags
flags = ["IS_ACTIVITY", "PAY_SEPARATELY", "ON_HOLD"]
for flag in flags:
    cb = driver.find_element(By.NAME, f"FIELD_{flag}")
    cb.click()
    assert cb.is_selected(), f"Error: Checkbox {flag} failed to toggle."

# Step 6: Distribution and Notes
# Navigate to Distribution Tab
dist_tab = driver.find_element(By.XPATH, '//*[@data-qtip="Distribution"]')
dist_tab.click()

add_dist = driver.find_element(By.XPATH, '//*[@data-qtip="Add new distribution"]')
add_dist.click()

# Enter GL Account information
dist_acct = driver.find_element(By.NAME, "GL_ACCOUNT_ID")
type_like_human(dist_acct, "100-200-3000-01")
dist_acct.send_keys(Keys.TAB)

# Step 7: Submission Workflow
submit_bill = driver.find_element(By.XPATH, '//*[@data-qtip="Submit bill"]')
submit_bill.click()
print(f"✅ Bill {invoice_num} submitted successfully.")

# Step 8: Cleanup and Exit
driver.quit()