import discord
import asyncio

@asyncio.coroutine
def process_message(message, client):
    if message.content.startswith('!test'):
        counter = 0
        tmp = yield from client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        yield from client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!ggquiz'):
        yield from client.send_message(message.channel, 'http://kalavinka.co.uk/GUILTY/')
    elif message.content.startswith('!bbquiz'):
        yield from client.send_message(message.channel, 'http://kalavinka.co.uk/EMBER/')
    elif message.content.startswith('!bbreplays'):
        yield from client.send_message(message.channel, 'http://keeponblaz.in')
    elif message.content.startswith('!ggreplays'):
        yield from client.send_message(message.channel, 'http://keeponrock.in')
    elif message.content.startswith('!shutdown'):
        yield from client.logout()
