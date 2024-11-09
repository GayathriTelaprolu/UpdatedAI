import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = 'https://jaysindiankitchen.com/north-attleboro-jay-s-indian-kitchen-food-menu'

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

    # Open or create a CSV file to save the scraped data
    with open('jays_indian_kitchen_menu.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Item Name', 'Price', 'Description'])

        # Find all menu item blocks
        items = soup.find_all('div', class_='food-item-title')

        # Loop through each item
        for item in items:
            # Extract item name (inside <h3>)
            item_name = item.find('h3').get_text(strip=True)

            # Extract price (inside <div> with class 'food-price')
            price_div = item.find_next_sibling('div', class_='food-price')
            item_price = price_div.get_text(strip=True) if price_div else 'N/A'

            # Extract description (inside <div> with class 'food-item-description')
            description_div = item.find_next_sibling('div', class_='food-item-description')
            item_description = description_div.get_text(strip=True) if description_div else 'N/A'

            # Write the row for each item
            writer.writerow([item_name, item_price, item_description])

    print("Data has been successfully saved to 'jays_indian_kitchen_menu.csv'")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
