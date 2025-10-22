from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of your Kubernetes app
URL = "http://localhost:31077"

def open_browser():
    service = Service(r"C:\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(URL)
    return driver

# Test 1: Page Load
def test_page_load():
    driver = open_browser()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    assert "Registration" in driver.title or "Register" in driver.page_source
    print("Page load test passed")
    driver.quit()

# Test 2: Valid Registration
def test_valid_registration():
    driver = open_browser()

    # Fill the form fields
    driver.find_element(By.NAME, "full_name").send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
    driver.find_element(By.NAME, "username").send_keys("test_user")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.NAME, "confirm_password").send_keys("password123")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")
    driver.find_element(By.NAME, "dob").send_keys("01/01/2000")
    driver.find_element(By.NAME, "gender").send_keys("Male")
    driver.find_element(By.NAME, "address").send_keys("123 Main Street")

    # Click the Register button
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))
    )
    register_button.click()

    time.sleep(3)  # Increased wait time
    
    # Check for success message - made more flexible
    page_source = driver.page_source
    success_indicators = ["Success", "Registered", "success", "Registration successful"]
    
    found_success = False
    for indicator in success_indicators:
        if indicator in page_source:
            found_success = True
            break
    
    if found_success:
        print("Valid registration test passed")
    else:
        print("Registration may have failed. Page content:")
        print(page_source[:500])  # Print first 500 characters for debugging
        assert False, "Success message not found after registration"
    
    driver.quit()


# Run all tests
if __name__ == "__main__":
    test_page_load()
    test_valid_registration()
    print("All tests completed!")