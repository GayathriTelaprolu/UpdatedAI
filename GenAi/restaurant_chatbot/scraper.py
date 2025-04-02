from bs4 import BeautifulSoup
import requests

def scrape_and_save_content(urls, output_file):
    """
    Scrapes content from the given URLs and saves it to a text file.

    Args:
        urls (list): List of URLs to scrape.
        output_file (str): Path to the output text file.
    """
    all_contents = []

    for url in urls:
        url = url.strip()  # Clean up any extra spaces
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                body_text = soup.get_text(strip=True)
                all_contents.append(f"Content from {url}:\n{body_text}")
            else:
                all_contents.append(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            all_contents.append(f"Error retrieving content from {url}: {e}")

    # Combine all the texts into a single string, separated by new lines
    combined_contents = "\n\n".join(all_contents)

    # Save the combined content to a text file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(combined_contents)

    print(f"Scraped content has been saved to {output_file}")

# Example usage
if __name__ == "__main__":
    # URLs to scrape (can be modified as needed)
    urls_input = input("Enter URLs to scrape, separated by commas: ")
    urls = urls_input.split(',')

    # Specify the output file
    output_file = "scraped_content.txt"

    # Call the function to scrape and save content
    scrape_and_save_content(urls, output_file)
