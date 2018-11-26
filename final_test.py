import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print("bot is ready to run")
    await client.change_presence(game=discord.Game(name='with you'))



@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')

    if message.content=="hi":
        await client.send_message(message.channel,"{0.author.mention} hye there :tada:<:blobcookie:516669559906893825>".format(message))



client.run(os.getenv('TOKEN))
