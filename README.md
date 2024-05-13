# News Discord Bot

This Discord bot fetches the top stories from Hacker News and posts them in your specified Discord channel.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Discord account and have created a bot on the Discord Developer Portal.
- You have installed Python 3.8 or higher on your machine.

## Setup Instructions

Follow these steps to set up the News Discord Bot:

1. **Clone the repository:**

```bash
git clone https://github.com/EthanM97/news-discord-bot.git
cd news-discord-bot
```

2. **Create a virtual environment:**

For Unix/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure your bot:**

Open the `news_bot.py` file and replace `YOUR_BOT_TOKEN` with your actual Discord bot token.

5. **Run the bot:**

```bash
python news_bot.py
```

## Commands

- `!greeting`: The bot will respond with a greeting message.
- `!news`: The bot fetches and posts the top stories from Hacker News.
- `!clear`: The bot will clear the last 50 messages in the channel.
