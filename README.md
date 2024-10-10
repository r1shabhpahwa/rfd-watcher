# RedFlagDeals RSS Monitor

This Python script monitors the **RedFlagDeals "Hot Deals"** RSS feed and sends new post notifications via **Pushover**.

## Features
- Checks for new deals every minute.
- Sends Pushover notifications with post details.
- Docker support for easy deployment.

## Requirements
- Pushover account (get your `PUSHOVER_TOKEN` and `PUSHOVER_USER_KEY`).
- Optional: Docker for containerized use.

## Setup

### Local
1. Clone the repo:  
   ```bash
   git clone https://github.com/yourusername/rfd-watcher.git
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables in the .env file:  
   ```bash
   PUSHOVER_TOKEN=your_token
   PUSHOVER_USER_KEY=your_key
   FILTER_KEYWORDS=Amazon.ca, ATL, Apple   #Optional
   WAIT_TIME=300   #Optional
   ```
4. Run the script:  
   ```bash
   python rfd_watcher.py
   ```

### Docker
1. Pull the image from Docker Hub:  
   ```bash
   docker pull rishabhpahwa/rfd_watcher_image
   ```
2. Run the Docker container:  
   ```bash
   docker run -d -e PUSHOVER_TOKEN=your_token -e PUSHOVER_USER_KEY=your_key rishabhpahwa/rfd_watcher_image
   ```
