import logging
import os
import time
import xml.etree.ElementTree as ET

import requests
import urllib3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure logging
logging.basicConfig(filename="rss_watcher.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Read Pushover credentials from environment variables
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")

# Read filter keywords from the environment variable
FILTER_KEYWORDS = os.getenv("FILTER_KEYWORDS")

# If FILTER_KEYWORDS is not None, split it into a list, else keep it as an empty list
if FILTER_KEYWORDS:
    filter_keywords = [keyword.strip().lower() for keyword in FILTER_KEYWORDS.split(',')]
else:
    filter_keywords = []

# Read the wait time between feed checks from the environment variable
# If not provided, default to 60 seconds
WAIT_TIME = int(os.getenv("WAIT_TIME", 120))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

seen_posts = set()

first_run = True


def send_initial_notification():
    response = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": PUSHOVER_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": "Watcher is active and monitoring the RSS feed.",
            "title": "RSS Feed Watcher"
        }
    )
    logging.info("~ Watcher started - Jai Shree Ram ~")


def send_notification(title, link):
    message = f"New Post: {title}\nLink: {link}"
    response = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": PUSHOVER_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message,
            "title": "RedFlagDeals Hot Deal"
        }
    )
    if response.status_code == 200:
        logging.info(f"Notification sent for post: {title}")
    else:
        logging.info(f"Failed to send notification: {response.status_code}")


def check_feed():
    global first_run
    # Fetch the RSS feed while bypassing SSL verification and using custom headers
    feed_url = "https://forums.redflagdeals.com/feed/forum/9"
    response = requests.get(feed_url, headers=headers, verify=False)

    # Check if the request was successful
    if response.status_code != 200:
        logging.error(f"Failed to fetch the feed. Status code: {response.status_code}")
        return

    # Check if the content is not empty
    if not response.content:
        logging.error("No content found in the response.")
        return

    # Parse the XML content
    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        logging.error(f"Error parsing XML: {e}")
        return

    # Atom namespace (as it's an Atom feed)
    namespace = {'atom': 'http://www.w3.org/2005/Atom'}

    # Find and process each post
    for entry in root.findall('atom:entry', namespace):
        title = entry.find('atom:title', namespace).text
        link = entry.find('atom:link', namespace).attrib['href']
        post_id = entry.find('atom:id', namespace).text

        # If it's the first run, just mark posts as seen without sending notifications
        if first_run:
            seen_posts.add(post_id)
        # Send notification for new posts only after the first run
        elif post_id not in seen_posts:
            # Check if filtering is required
            if not filter_keywords or any(keyword in title.lower() for keyword in filter_keywords):
                send_notification(title, link)
            seen_posts.add(post_id)

    # After the first run, set first_run to False
    if first_run:
        first_run = False


# Main loop to run the feed check every minute
def monitor_feed():
    while True:
        logging.info("Checking for new posts...")
        check_feed()
        time.sleep(WAIT_TIME)


if __name__ == "__main__":
    send_initial_notification()
    monitor_feed()
