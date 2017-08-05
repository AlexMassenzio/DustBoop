import discord
import asyncio
import sys

from message_handler import process_message

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
    print(message.author.name + ": " + message.content)
    yield from process_message(message, client)


#first command-line argument should be the token
client.run(sys.argv[1])