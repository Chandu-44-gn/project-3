import requests
from bs4 import BeautifulSoup

# Step 1: Download the webpage
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all quote containers
quote_blocks = soup.find_all('div', class_='quote')

# Step 4: Loop through each quote and extract text and author
for quote in quote_blocks:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f'"{text}" — {author}')
