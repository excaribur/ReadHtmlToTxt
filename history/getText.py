from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver (automatically download ChromeDriver using webdriver_manager)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1: Open the login page
login_url = "https://app.ilovejapanschool.com/login"  # Replace with the correct login URL
driver.get(login_url)

# Step 2: Enter login credentials
username = driver.find_element(By.NAME, "email")  # Replace with the correct input name or ID
password = driver.find_element(By.NAME, "password")  # Replace with the correct input name or ID

# Replace with your actual credentials
#Username : sensei@esp-group.asia
#Password: Espjapanese1234
username.send_keys("sensei@esp-group.asia")
password.send_keys("Espjapanese1234")

# Step 3: Submit the login form
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Adjust the selector as needed
login_button.click()

# Optional: Wait for the page to load after login
time.sleep(5)

# Step 4: Navigate to the target page
target_url = "https://app.ilovejapanschool.com/course/basic-japanese-grammar-course/CVU5106338"
driver.get(target_url)
time.sleep(5)

# Step 4: Locate and click the "chrome_reader_mode" icon
try:
    icon_element = driver.find_element(By.CSS_SELECTOR, "div.attachments a.showDescIcon i.showDescIcon_icon")
    icon_element.click()
    print("Icon clicked successfully!")
except Exception as e:
    print(f"Error: {e}")

# Optional: Wait for the content to load after clicking
time.sleep(3)


# Close the browser
#driver.quit()
