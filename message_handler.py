import discord
import asyncio
import subprocess
import aiohttp
import json

@asyncio.coroutine
def process_message(message, client):
    if message.content.startswith('!help'):
        with open('data/help.json') as json_data:
            help_data = json.load(json_data)
            command_string = 'List of DustBoop Commands:\n'
            for command in help_data['commands']:
                command_string += '!' + command['name'] + ' - ' + command['description'] + '\n'
            yield from client.send_message(message.channel, command_string)
    elif message.content.startswith('!ggquiz'):
        yield from client.send_message(message.channel, 'http://kalavinka.co.uk/GUILTY/')
    elif message.content.startswith('!bbquiz'):
        yield from client.send_message(message.channel, 'http://kalavinka.co.uk/EMBER/')
    elif message.content.startswith('!bbreplays'):
        yield from client.send_message(message.channel, 'http://keeponblaz.in')
    elif message.content.startswith('!ggreplays'):
        yield from client.send_message(message.channel, 'http://keeponrock.in')
    elif message.content.startswith('!test'):
        url = 'http://www.dustloop.com/wiki/api.php?action=parse&format=json&page=BBCF%2FHibiki_Kohaku&prop=displaytitle'
        response = yield from aiohttp.request('get', url)
        string = (yield from response.read()).decode('utf-8')
        data = json.loads(string)
        answer = data['parse']['displaytitle']
        yield from client.send_message(message.channel, answer + '\nhttp://www.dustloop.com/wiki/images/8/8d/BBCF_Hibiki_2A.png')
    elif message.content.startswith('!restart'):
        yield from client.send_message(message.channel, 'Restarting...')
        subprocess.call(['shutdown', '-r', 'now'])
        yield from client.logout()
