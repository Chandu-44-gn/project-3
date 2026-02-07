import requests
from bs4 import BeautifulSoup

# Step 1: Download the webpage
url = "https://notes.iamdev.in/com"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all the links
links = soup.find_all('a')

# Step 4: Print the links
for link in links:
    href = link.get('href')
    print(href)