import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os


client =  commands.Bot(command_prefix=';')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print("bot is ready to run")
    await client.change_presence(game=discord.Game(name='with you'))



@client.event
async def on_message(message):
    if message.content.startswith('ping'):
       await client.send_message(message.channel, 'Pong!<:pepePunch:516721734607699968>')
    if message.content=="hi":
        await client.send_message(message.channel,"{0.author.mention} hye there :tada:<:blobcookie:516669559906893825>".format(message))

    await client.process_commands(message)
    
@client.command()
async def echo(*args):
    output =' '
    for word in args:
        output +=word
        output +=' '
    await client.say(output)
    
@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Calculating Heartbeat')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Pong!<:pepePunch:516721734607699968>: my heartbeat is: {}ms:heartpulse:'.format(int(ms)))


client.run(os.getenv('TOKEN'))
