import discord
import asyncio
import subprocess
import aiohttp
import json

@asyncio.coroutine
def character_preview(message, client):
	 with open('data/character.json') as json_data:
        character_data = json.load(json_data)
        for character in help_data['characters']:
            #implement lookup here
        yield from client.send_message(message.channel, "TBD")