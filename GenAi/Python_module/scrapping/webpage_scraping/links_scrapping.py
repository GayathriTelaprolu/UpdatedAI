import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from urllib.parse import urljoin, urlparse

# Set headers to simulate a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# Function to scrape data from a URL and save to a PDF using ReportLab
def scrape_to_pdf(url, pdf_filename):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract all the text data on the page
            page_text = soup.get_text(separator='\n', strip=True)

            # Create a PDF with ReportLab
            c = canvas.Canvas(pdf_filename, pagesize=letter)
            width, height = letter

            # Add a title (URL) at the top of the PDF
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(width / 2.0, height - 40, f"Scraped Data from: {url}")

            # Move down and start writing the content
            c.setFont("Helvetica", 12)
            text_object = c.beginText(40, height - 80)  # Starting position

            # Set line spacing and margins
            text_object.setLeading(14)

            # Add text line by line, with handling for page breaks
            lines = page_text.split("\n")
            for line in lines:
                if len(line.strip()) > 0:  # Ignore empty lines
                    text_object.textLine(line.strip())
                    # Check if the text reaches the bottom of the page
                    if text_object.getY() < 50:
                        c.drawText(text_object)
                        c.showPage()  # Start a new page
                        text_object = c.beginText(40, height - 80)  # Reset position

            # Finish writing the text and save the PDF
            c.drawText(text_object)
            c.save()
            print(f"Data scraped and saved to {pdf_filename}")
        else:
            print(f"Failed to scrape {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

# Function to check if a URL is internal and valid
def is_valid_internal_link(url, base_url):
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(url).netloc
    return (link_domain == base_domain or link_domain == '') and not url.startswith('javascript:') and not url.startswith('mailto:')

# Function to scrape each link from a list of URLs in a text file
def scrape_from_links_file(links_file, base_url):
    if not os.path.exists(links_file):
        print(f"The file {links_file} does not exist.")
        return

    # Create a directory for storing PDFs if it doesn't exist
    if not os.path.exists('scraped_pdfs'):
        os.makedirs('scraped_pdfs')

    # Open the text file containing the links
    with open(links_file, 'r') as file:
        links = file.readlines()

    # Open a text file to save external links that can't be scraped
    with open('external_links.txt', 'w', encoding='utf-8') as external_file:
        for url in links:
            url = url.strip()
            full_url = urljoin(base_url, url)  # Handle relative URLs

            # Check if it's a valid internal link
            if is_valid_internal_link(full_url, base_url):
                # Generate a PDF filename based on the URL
                pdf_filename = os.path.join('scraped_pdfs', f"{url.replace('/', '_')}.pdf")
                
                # Scrape the internal URL and save to PDF
                scrape_to_pdf(full_url, pdf_filename)
            else:
                # Write external links or invalid links to the text file
                external_file.write(f"This is out of the website, I can't scrape it: {full_url}\n")

    print("Scraping completed. External links saved to 'external_links.txt'.")

# Run the scraper using the scraped links file
links_file = 'scraped_links.txt'  # Assuming you saved the links to this file
base_url = 'https://jaysindiankitchen.com/'
scrape_from_links_file(links_file, base_url)
