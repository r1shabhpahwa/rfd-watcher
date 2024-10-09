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
- **Docker**: If you plan to run the application in a Docker container, ensure Docker is installed. You can download Docker from [here](https://docs.docker.com/get-docker/).

## Setup and Usage

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/rfd-watcher.git
cd rfd-watcher
```

### 2. Install dependencies:

If you're running the script without Docker, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set Your Pushover Credentials

You need to set the following environment variables in your system:

- `PUSHOVER_TOKEN`: Your Pushover application's API token.
- `PUSHOVER_USER_KEY`: Your Pushover user key.

You can set these using the terminal:

```bash
export PUSHOVER_TOKEN=your_pushover_token
export PUSHOVER_USER_KEY=your_pushover_user_key
```

### 4. Run the Script

You can run the script locally:

```bash
python rfd_watcher.py
```

### 5. Run with Docker

#### Step 1: Build the Docker Image

If you'd like to run the application inside a Docker container, first build the image:

```bash
docker build -t rfd_watcher_image .
```

#### Step 2: Run the Docker Container

You can pass your Pushover credentials as environment variables when running the container:

```bash
docker run -d \
  -e PUSHOVER_TOKEN=your_pushover_token \
  -e PUSHOVER_USER_KEY=your_pushover_user_key \
  rfd_watcher_image
```

Alternatively, you can use an `.env` file to store your credentials:

1. Create a `.env` file:

```bash
PUSHOVER_TOKEN=your_pushover_token
PUSHOVER_USER_KEY=your_pushover_user_key
```

2. Run the container with the `.env` file:

```bash
docker run --env-file .env -d rfd_watcher_image
```

### 6. Check Logs

To see logs from the running container:

```bash
docker logs <container_id>
```

### 7. Stopping the Container

To stop the container, you can use the `docker stop` command:

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
