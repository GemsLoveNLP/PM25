from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get("http://air4thai.pcd.go.th/webV3/#/History")

# Wait for the user to manually make selections
print("Please complete the checkbox selections manually. Press Enter here to continue...")
input()

# Now the script resumes after manual selections
try:
    # Get the page HTML and prettify it using BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    pretty_html = soup.prettify()

    # Write the prettified HTML to a file
    with open('_.html', 'w', encoding='utf-8') as file:
        file.write(pretty_html)

    print("The HTML has been saved to _.html.")

except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()
