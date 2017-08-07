import discord
import asyncio
import subprocess

@asyncio.coroutine
def process_message(message, client):
    if message.content.startswith('!ggquiz'):
        yield from client.send_message(message.channel, 'http://kalavinka.co.uk/GUILTY/')
    elif message.content.startswith('!bbquiz'):
        yield from client.send_message(message.channel, 'http://kalavinka.co.uk/EMBER/')
    elif message.content.startswith('!bbreplays'):
        yield from client.send_message(message.channel, 'http://keeponblaz.in')
    elif message.content.startswith('!ggreplays'):
        yield from client.send_message(message.channel, 'http://keeponrock.in')
    elif message.content.startswith('!restart'):
        subprocess.call(['shutdown', '-r', 'now'])
        yield from client.logout()
