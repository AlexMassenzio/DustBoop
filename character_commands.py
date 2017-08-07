import discord
import asyncio
import subprocess
import aiohttp
import json

@asyncio.coroutine
def character_preview(message, client):
	 with open('data/character.json') as json_data:
	 	if message.split().length < 2:
	 		yield from client.send_message(message.channel, "Please inclue a character name")
	 		return

	 	character_name = message.split()[1]
        character_data = json.load(json_data)
        for character in help_data['characters']:
            if character_name == character['name']:
        	yield from client.send_message(message.channel, character['title'])
            	