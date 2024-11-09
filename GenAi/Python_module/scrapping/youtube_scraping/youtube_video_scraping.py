import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from textblob import TextBlob

# Set the path to the manually downloaded ChromeDriver
chromedriver_path = 'C:/Users/HP/chromedriver.exe'  # Update this path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open the YouTube video page
video_url = 'https://www.youtube.com/watch?v=6R0TkF6Mgrk'  # Replace with the actual video URL
driver.get(video_url)

# Wait for the page to load and comments to appear
try:
    # Wait until the comments section is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'ytd-comments'))
    )
except Exception as e:
    print("Could not find comments section:", e)

# Scroll down to load comments
scroll_pause_time = 2  # Adjust based on your internet speed
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait to load more comments
    time.sleep(scroll_pause_time)

    # Calculate new scroll height and compare with the last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Extract comments and usernames using JavaScript
comments_data = driver.execute_script("""
    let comments = [];
    let comment_elements = document.querySelectorAll('ytd-comment-thread-renderer #content-text');
    let username_elements = document.querySelectorAll('ytd-comment-thread-renderer #author-text span');

    for (let i = 0; i < comment_elements.length; i++) {
        let comment = comment_elements[i].innerText;
        let username = username_elements[i].innerText;
        comments.push({username: username, comment: comment});
    }
    return comments;
""")

# Check if comments_data is empty
if not comments_data:
    print("No comments found or the structure might have changed.")
else:
    # Analyze sentiment for each comment and create a list of dictionaries
    scraped_data = []
    for data in comments_data:
        comment = data['comment']
        username = data['username']
        
        # Perform sentiment analysis
        blob = TextBlob(comment)
        sentiment = blob.sentiment
        
        # Append username, comment, polarity, and subjectivity to the list
        scraped_data.append({
            'Username': username,
            'Comment': comment,
            'Polarity': sentiment.polarity,
            'Subjectivity': sentiment.subjectivity
        })

    # Create a pandas DataFrame
    df = pd.DataFrame(scraped_data)

    # Save the DataFrame to a CSV file
    df.to_csv('youtube_comments_sentiment_analysis.csv', index=False)

    print("Scraping complete. Data saved to youtube_comments_sentiment_analysis.csv")

# Close the browser
driver.quit()
