import discord
import time
from discord.ext import commands
client = discord.Client()
message_number = 0

token = "TOKEN HERE" # Insert your 0auth token here
start = "START MESSAGE" # What is the trigger command
message = "SPAM MESSAGE" # What message to spam
amount = 69 # How many times should the message repeated
delay = 5 # Delay between messages


@client.event
async def on_ready():
    print(f'Ready! Start spamming with {start}')

@client.event
async def on_message(message):


    if message.content.startswith(f'{start}'):

      while message_number <= amount:  
        await message.channel.send(f'{message}')
        print("Sent")
        time.sleep(delay)
        
 
print("Done spamming.")
client.run(token)
