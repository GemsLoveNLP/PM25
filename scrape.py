# import requests
# from bs4 import BeautifulSoup

# # Get the initial page
# url = "http://air4thai.pcd.go.th/webV3/#/History"
# # headers = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# # }

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # # Example: Extracting all rows from a table
# # rows = soup.select("table tr")  # Adjust the selector based on your page structure

# # for row in rows:
# #     columns = row.find_all("td")  # Adjust tag if needed
# #     row_data = [col.text.strip() for col in columns]
# #     print(row_data)

# print(soup.prettify())  # Print the HTML content for debugging

# -----------------------

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://example.com",  # Some APIs require this
    "Accept": "application/json"  # Adjust based on what you see in Network tab
}

api_url = "http://air4thai.pcd.go.th/webV3/#/History"  # Replace with the actual API URL
params = {
    "page": 1,  # If there are pagination params, include them here
    "limit": 50
}

response = requests.get(api_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()  # or response.text if it's not JSON
    print(data)
else:
    print(f"Failed to fetch data: {response.status_code}")

