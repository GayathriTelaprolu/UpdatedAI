import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://jaysindiankitchen.com/'

# Set headers to simulate a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# Send HTTP request to the URL
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags with href attribute
    links = soup.find_all('a', href=True)

    # Open or create a text file to save the scraped links
    with open('scraped_links.txt', mode='w', encoding='utf-8') as file:
        for link in links:
            # Get the href (URL) from the <a> tag
            url = link['href']
            # Write each URL on a new line
            file.write(url + '\n')

    print("Links have been successfully saved to 'jays_indian_kitchen_homepage_links.txt'")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
