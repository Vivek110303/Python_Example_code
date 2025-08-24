from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -- Replace these with your actual credentials --
EMAIL = "yi.trevelle@lvory.org"
PASSWORD = "demousertest123"
STATUS_MESSAGE = "Hi there"

# Start a new Firefox browser session
driver = webdriver.Firefox()

try:
    driver.get("https://www.facebook.com/")

    # Wait until the email field is present, then send email
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_element.send_keys(EMAIL)

    # Wait until the password field is present, then send password
    pass_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    pass_element.send_keys(PASSWORD)

    # Click the login button
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "loginbutton"))
    )
    login_btn.click()

    # Wait for the status message input to appear
    status_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "xhpc_message"))
    )
    status_element.send_keys(STATUS_MESSAGE)

    # Wait for possible buttons
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    buttons = driver.find_elements(By.TAG_NAME, "button")

    # Find and click the "Post" button
    for button in buttons:
        if button.text.strip().lower() == "post":
            button.click()
            break

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser after all actions are complete
    driver.quit()
