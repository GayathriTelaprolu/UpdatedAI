from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Replace with your ChromeDriver path
driver_path = 'C:/Users/HP/chromedriver.exe'

# Setup options for headless browsing (if desired)
options = Options()
# options.add_argument('--headless')  # Uncomment if you want to run in headless mode

# Setup driver
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# List to store results
results = []
column_names = []  # Declare column_names here

# Function to select the "Graduate" region and the "ApplicationID" search type
def select_graduate_region_and_search_type():
    try:
        # Select the 'Graduate' tab
        graduate_tab = driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="#Graduate"]')
        graduate_tab.click()
        time.sleep(1)

        # Select the 'ApplicationID' radio button
        application_id_radio = driver.find_element(By.ID, 'GraduateAppID')
        application_id_radio.click()

    except Exception as e:
        print(f"Error selecting graduate region or search type: {e}")

# Function to input the application ID and search
def search_by_application_id(application_id):
    try:
        # Input the application ID in the search field
        input_field = driver.find_element(By.ID, 'TextBox2')
        input_field.clear()
        input_field.send_keys(application_id)
        
        # Click the 'Search' button
        search_button = driver.find_element(By.ID, 'btnGraduates')
        search_button.click()

        # Wait for the results table to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'table'))
        )

    except Exception as e:
        print(f"Error searching for application ID {application_id}: {e}")

# Function to scrape the entire row for the given application ID
def scrape_data_for_application():
    global column_names  # Declare as global to access in other parts of the code
    try:
        # Locate the table
        table = driver.find_element(By.TAG_NAME, 'table')

        # Locate the header to get the column names
        headers = table.find_elements(By.TAG_NAME, 'th')
        column_names = [header.text for header in headers]  # Save column names globally

        # Locate all rows in the table
        rows = table.find_elements(By.TAG_NAME, 'tr')

        # Loop through all rows and scrape the data
        for row in rows[1:]:  # Skip header row
            # Get all the cells in the row
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:  # Only append non-empty rows
                row_data = [cell.text for cell in cells]
                results.append(row_data)

        # Print the results for debugging
        print(f"Scraped data for application ID: {results[-1]}")  # Show last scraped row

    except Exception as e:
        print(f"Error scraping data: {e}")

# Open the website
driver.get('https://ceoaperolls.ap.gov.in/AP_MLC_2024/ERO/Status_Update_2024/knowYourApplicationStatus.aspx')

# Iterate over application IDs (incrementing by 1) and scrape up to 10 IDs
for i in range(11,21):
    # Increment the application ID
    application_id = f'F18-{str(i).zfill(7)}'
    
    # Select the region and search type
    select_graduate_region_and_search_type()
    
    # Search using the application ID
    search_by_application_id(application_id)
    
    # Scrape the data for the current application ID
    scrape_data_for_application()

    # Sleep for a bit before the next iteration (to avoid overwhelming the server)
    time.sleep(2)

# Convert the results to a DataFrame with dynamic column names
df = pd.DataFrame(results, columns=column_names)  # Use the captured column names

# Save the results to a CSV file
df.to_csv('application_status_results_full_table.csv', index=False)

# Close the browser
driver.quit()

print("Scraping completed and results saved to application_status_results_full_table.csv")  
