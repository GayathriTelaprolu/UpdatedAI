import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Function to scrape data from a page
def scrape_jobs(page_url):
    driver.get(page_url)
    time.sleep(3)  # Wait for the page to load
    
    # Using the corrected CSS selectors for job titles and company names
    job_titles = driver.find_elements(By.CSS_SELECTOR, 'a.card-title-link')
    company_names = driver.find_elements(By.CSS_SELECTOR, 'a[data-cy="search-result-company-name"]')
    locations = driver.find_elements(By.CSS_SELECTOR, '#searchDisplay-div > div:nth-child(3) > dhi-search-cards-widget > div > dhi-search-card > div > div.card-header > div > div.d-flex.justify-content-between.title-container > div.overflow-hidden > div > span')
    job_types = driver.find_elements(By.CSS_SELECTOR, '#searchDisplay-div > div:nth-child(3) > dhi-search-cards-widget > div > dhi-search-card > div > div.card-body.font-small.m-left-20.mobile-m-left-10 > div.d-flex.flex-wrap > div.card-position-type > span')
    
    jobs = []
    
    for i in range(len(job_titles)):
        job_data = {
            'Job Title': job_titles[i].text if i < len(job_titles) else 'N/A',
            'Company Name': company_names[i].text if i < len(company_names) else 'N/A',
            'Location': locations[i].text if i < len(locations) else 'N/A',
            'Job Type': job_types[i].text if i < len(job_types) else 'N/A'
        }
        jobs.append(job_data)
    
    return jobs

# List to hold all job data
all_jobs = []

# Define the base URL
base_url = "https://www.dice.com/jobs?q=python%20developer&countryCode=US&radius=30&radiusUnit=mi&page={}&pageSize=100&filters.postedDate=ONE&language=en&utm_source=google&utm_medium=paid_search&utm_campaign=B2C_Brand_General&utm_term=dice&utm_content=70736557127&gclid=CjwKCAjw3624BhBAEiwAkxgTOoXfUJwwbcTJkjiOvHPvz-WiMuvIz_dSJo21kHib3A72Irb053_JwRoCtqsQAvD_BwE"

# Start scraping from page 1
page = 1

while True:
    page_url = base_url.format(page)
    print(f"Scraping page {page}: {page_url}")
    jobs_on_page = scrape_jobs(page_url)
    
    # If no jobs are found on the current page, break the loop
    if not jobs_on_page:
        print(f"No more jobs found on page {page}. Exiting.")
        break
    
    all_jobs.extend(jobs_on_page)
    page += 1

# Convert the data into a DataFrame
df = pd.DataFrame(all_jobs)

# Save to CSV
df.to_csv('job_listings_all_pages_corrected.csv', index=False)

print("Data scraping completed and saved to 'job_listings_all_pages_corrected.csv'")

# Close the driver
driver.quit()
