import discord
import os
import datetime
from datetime import datetime
import random
import pytz
import asyncio


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(".Help"):
    await message.channel.send("Try using : .Help .Hello .Delete .Time .Coinflip .Morning")
    
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
  
client.run(os.environ['KEY'])

