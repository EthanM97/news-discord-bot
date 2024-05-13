# Standard library imports
import asyncio

# Related third-party imports
import aiohttp
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import requests
import scrapy

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
CHANNEL_ID = 'YOUR_CHANNEL_ID_HERE' # Replace with your channel ID which is an int

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def get_webpage(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    print(f"Failed to fetch page with status: {response.status}")
                    return None
        except Exception as e:
            print(f"Error fetching webpage: {e}")
            return None

def parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    story_links = soup.find_all('span', class_='titleline')

    news_list = []
    for link in story_links[:12]:  # Process only the first 12 links
        story_url = link.a['href']
        story_title = link.a.text
        news_list.append(f"**Title:** {story_title}\n**Link:** {story_url}\n\n---\n\n")  # Added markdown for bold and more line breaks
    return "\n".join(news_list)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))  # Improved login message
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("News Bot online!")
    await channel.send("Type `!greeting` to get started.")

@bot.command()
async def greeting(ctx):
    await ctx.send("Hi! I'm a news bot created to send you the top 12 stories on Hacker News.")
    await ctx.send("To get the news, type `!news` or `!clear` to remove messages.")

@bot.command()
async def clear(ctx, limit: int = 50):
    if limit > 50:  # Discord API allows deleting up to 100 messages at a time
        limit = 50
    await ctx.channel.purge(limit=limit + 1)  # +1 to include the command message itself
    await ctx.send(f'Cleared {limit} messages.', delete_after=.5)  # The confirmation message will auto-delete after 5 seconds

@bot.command()
async def news(ctx):
    await ctx.send("Here are the top 12 stories on Hacker News:")
    url = 'https://news.ycombinator.com/newest'
    html = await get_webpage(url)  # Assuming get_webpage is already asynchronous
    if html: # html is true then
        news_data = parser(html) # parse the html
        if news_data: # if that is true
            for news_item in news_data.split('---\n\n'):  # Use the dashes as split points
                if news_item.strip():  # Check if there is any text to send
                    await ctx.send(news_item)  # Send one item
                    await asyncio.sleep(.5)  # Wait for 1/2 second to avoid rate limits and for readability
        else: # Error message
            await ctx.send("No news stories found.")
    else: # Error message
        await ctx.send("Failed to fetch news.")

bot.run(BOT_TOKEN)
