import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create a Service object
service = Service('C:/Users/HP/chromedriver.exe')  # Update with your chromedriver path

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Specify the URL to scrape
url = "https://www.dice.com/jobs?q=python%20developer&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=100&language=en&utm_source=google&utm_medium=paid_search&utm_campaign=B2C_Brand_General&utm_term=dice&utm_content=70736557127&gclid=CjwKCAjw3624BhBAEiwAkxgTOoXfUJwwbcTJkjiOvHPvz-WiMuvIz_dSJo21kHib3A72Irb053_JwRoCtqsQAvD_BwE"

# Load the webpage
driver.get(url)

# Wait for the page to load
time.sleep(5)

# List to store job data
job_data = []

# Scrape job listings
try:
    # Find job elements
    jobs = driver.find_elements(By.CSS_SELECTOR, '#searchDisplay-div > div:nth-child(3) > dhi-search-cards-widget > div > dhi-search-card')
    
    for job in jobs:
        try:
            # Extracting job information using updated CSS selectors
            job_name = job.find_element(By.CSS_SELECTOR, 'div.card-header a').text.strip()  # Job name
            company_name = job.find_element(By.CSS_SELECTOR, 'div.overflow-hidden > div > a').text.strip()  # Company name
            job_location = job.find_element(By.CSS_SELECTOR, 'div.overflow-hidden > div > span').text.strip()  # Job location
            job_type = job.find_element(By.CSS_SELECTOR, 'div.card-position-type span').text.strip()  # Job type
            
            # Append the job data to the list
            job_data.append([job_name, company_name, job_location, job_type])
        except Exception as e:
            print(f"An error occurred while scraping job data: {e}")

    # Save the job data to a CSV file
    if job_data:
        with open('job_listings.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Job Name', 'Company Name', 'Location', 'Job Type'])  # Write the header
            writer.writerows(job_data)  # Write the job data
        print(f"Scraped {len(job_data)} job listings and saved to job_listings.csv")
    else:
        print("No job data found to save.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    driver.quit()
