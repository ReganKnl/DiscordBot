import discord
import os
import datetime
from datetime import datetime
import random
import pytz
import asyncio
import requests

intents = discord.Intents.all()
client = discord.Client(intents=intents)

GOOGLE_API_KEY = 'AIzaSyAhQEc00S7CkplAh5xUOEICcRmnzYCZNW8'
SEARCH_ENGINE_ID = 'c68361963bf044d3f'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".Help"):
        await message.channel.send("Try using : .Help .Hello .Delete .Time .Coinflip .Morning .Google")

    if message.content.startswith(".Hello"):
        await message.channel.send("Hi")

    if message.content.startswith(".Time"):
        current_time = datetime.now(pytz.timezone('Asia/Jakarta'))
        realtime = current_time.strftime('%H:%M:%S')
        await message.channel.send(realtime)

    if message.content.startswith(".Delete"):
        parts = message.content.split()
        if len(parts) == 2:
            try:
                num_messages_to_delete = int(parts[1])
            except ValueError:
                pass
            messages_to_delete = [message]
            async for message_to_delete in message.channel.history(limit=num_messages_to_delete):
                messages_to_delete.append(message_to_delete)
                await message_to_delete.delete()
                await asyncio.sleep(1)

    if message.content.startswith(".Coinflip"):
        choice = message.content.split()[1].lower()
        if choice not in ["heads", "tails"]:
            await message.channel.send("Please choose 'Heads' or 'Tails'.")
            return

        result = random.choice(["Heads", "Tails"])

        await message.channel.send(f"Bot rolled {result}")

        if result.lower() == choice:
            await message.channel.send("WWWW")
        else:
            await message.channel.send("LLLL")

    if message.content.startswith(".Morning"):
        await message.channel.send("THIS MORNING I WOKE UP TODAY IN THIS MORNING.IN THE MORNING I WOKE UP THIS MORNING I WOKE UP AND REMEMBER THAT EVERY MORNING THAT I WAKE UP I WILL.I WOKE UP THAT DAY JUST REMEMBER THAT")

    if message.content.startswith(".Google"):
        query = message.content[7:].strip()
        if query:
            search_results = google_search(query)
            await message.channel.send(search_results)
        else:
            await message.channel.send("Please provide a search query after .Google")

def google_search(query):
  search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"
  response = requests.get(search_url)

  if response.status_code == 200:
      results = response.json()
      items = results.get("items", [])

      if items:
          top_result = items[0] 
          title = top_result.get("title", "No title available")
          link = top_result.get("link", "No link available")
          return f"Here is the link you asked:\n{title}: {link}"
      else:
          return "No search results found."
  else:
      return "Error: Unable to perform the Google search."


client.run('MTE3MDk5MjE2MzE3NDIyMzkwMg.GQeQ1y.5UhDap9axyQrbhCphjxVYK23RntXIj80gDjviA')
