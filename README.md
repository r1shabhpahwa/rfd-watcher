---

# RedFlagDeals RSS Monitor

This Python project monitors the **RedFlagDeals "Hot Deals" forum** RSS feed and sends notifications for new posts via **Pushover**. It runs continuously, checking the feed every minute and notifying users of any new deals that haven't been seen before.

## Features

- **Monitors RSS Feed**: Automatically checks the RedFlagDeals "Hot Deals" forum for new posts every minute.
- **Pushover Notifications**: Sends a Pushover notification containing the post title and link of each new deal.
- **Dockerized**: Easily deploy the application using Docker for consistent performance across environments.
- **Customizable**: Users can pass in their own Pushover API credentials.

## Requirements

- **Pushover account**: You'll need to create a Pushover application and obtain your `PUSHOVER_TOKEN` and `PUSHOVER_USER_KEY`. Visit [Pushover](https://pushover.net/) to create your account.
- **Docker** (optional): If you plan to run the application in a Docker container, ensure Docker is installed. You can download Docker from [here](https://docs.docker.com/get-docker/).

## Setup and Usage

### Option 1: Run Locally (Without Docker)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rfd-watcher.git
cd rfd-watcher
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Pushover credentials as environment variables:

```bash
export PUSHOVER_TOKEN=your_pushover_token
export PUSHOVER_USER_KEY=your_pushover_user_key
```

4. Run the script:

```bash
python rfd_watcher.py
```

### Option 2: Run with Docker

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rfd-watcher.git
cd rfd-watcher
```

2. Build the Docker image:

```bash
docker build -t rfd_watcher_image .
```

3. Run the Docker container, passing your Pushover credentials as environment variables:

```bash
docker run -d \
  -e PUSHOVER_TOKEN=your_pushover_token \
  -e PUSHOVER_USER_KEY=your_pushover_user_key \
  rfd_watcher_image
```

Alternatively, use an `.env` file for your credentials:

1. Create a `.env` file with your credentials:

```bash
PUSHOVER_TOKEN=your_pushover_token
PUSHOVER_USER_KEY=your_pushover_user_key
```

2. Run the Docker container using the `.env` file:

```bash
docker run --env-file .env -d rfd_watcher_image
```

### Checking Logs and Stopping the Docker Container

To view logs from the running container:

```bash
docker logs <container_id>
```

To stop the container:

```bash
docker stop <container_id>
```

## Customization

You can customize the following in the code:

- **RSS Feed URL**: Modify the `feed_url` in the `rfd_watcher.py` file if you wish to monitor a different RSS feed.
- **Notification Timing**: Adjust the `time.sleep()` interval to change how often the feed is checked (currently set to 1 minute).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you’d like to contribute, feel free to submit pull requests or open issues. Contributions, bug reports, and feature requests are welcome!

## Support

For any questions or support, please create an issue in the [GitHub repo](https://github.com/yourusername/rfd-watcher) or contact me directly.

---

### Tags:
- `RedFlagDeals`
- `RSS Monitor`
- `Pushover Notifications`
- `Docker`

---
