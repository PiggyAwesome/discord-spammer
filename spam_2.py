

import discord
import time
from discord.ext import commands
client = discord.Client()


token = "TOKEN" # Insert your 0auth token here
start = "START MESSAGE" # What is the trigger command
megage = "SPAM MESSAGE" # What message to spam
amount = 69 # How many times should the message repeated
delay = 5 # Delay between messages


@client.event
async def on_ready():
    print(f'Ready! Start spamming with {start}')

@client.event
async def on_message(message):

    message_number = 0
    if message.content.startswith(f'{start}'):

       while message_number < amount: 
        await message.channel.send(megage)
        message_number += 1
        print(f"Sent message numer {str(message_number)}")
        time.sleep(delay)
        
    if message_number == amount: 
        print("Done spamming.")
client.run(token)
