from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Provide the path to your chromedriver
service = Service("C:/Users/Acer/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Update this path

# Launch the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to your test page (update path if needed)
driver.get("http://127.0.0.1:5501/test.html")  # Use your local file path

try:
    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Fill in the Name field
    name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    name_input.send_keys("John Doe")

    # Fill in the Email field
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("johndoe@example.com")

    # Fill in the Phone Number field
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.send_keys("9876543210")

    # Select the Country Code
    country_dropdown = driver.find_element(By.ID, "country")
    country_dropdown.click()
    country_option = driver.find_element(By.XPATH, "//option[@value='+44']")  # UK Country Code
    country_option.click()

    # Fill in the Password field
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Password123")

    # Agree to the terms and conditions
    terms_checkbox = driver.find_element(By.ID, "terms")
    terms_checkbox.click()

    # Click the Sign-Up button
    signup_button = driver.find_element(By.ID, "signup-button")
    signup_button.click()

    print("Sign-up form filled and submitted successfully!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
