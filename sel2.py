from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Set up Chrome options with SSL and security fixes
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument('--ssl-version-min=tls1.2')

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get("http://air4thai.pcd.go.th/webV3/#/History")

# Wait for the user to manually make selections
print("Please complete the checkbox selections manually. Press Enter here to continue...")
input()

# Create the 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

page_number = 1

while True:
    # Wait for the page to load completely (adjust time as needed)
    time.sleep(2)

    print("Processing page", page_number)

    # Get the HTML of the current page
    page_html = driver.page_source

    # Write the HTML to a file in the 'data' folder
    with open(f'data/{page_number}.html', 'w', encoding='utf-8') as file:
        file.write(page_html)

    # Wait for the "next page" button to become clickable
    try:
        # Wait until the "next page" button is clickable
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'page-item') and contains(@class, 'flex-fill')]//button[contains(@aria-label, 'Go to next page')]"))
        )

        # If the next button exists and is clickable, click it
        next_button.click()
        page_number += 1
    except Exception as e:
        # If there's no next button or the button is not clickable, we can stop
        print(f"End of pages or error: {e}")
        break

# Close the driver
driver.quit()
