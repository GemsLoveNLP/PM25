from bs4 import BeautifulSoup
import re

# Read the HTML file
with open('data/27.html', 'r', encoding='utf-8') as file:
      content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all <text> tags inside <g> elements
text_elements = soup.find_all("text")

# Extract station code and address using regex
data = []
pattern = re.compile(r"(\d+t) \((.+)\)")

for text in text_elements:
    match = pattern.search(text.text.strip())
    if match:
        station_code = match.group(1)
        thai_address = match.group(2)
        data.append((station_code, thai_address))

# Output the extracted list
print(data)
