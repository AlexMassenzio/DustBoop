import discord
import asyncio
import subprocess
import aiohttp
import json

@asyncio.coroutine
def character_preview(message, client):
	yield from client.send_message(message.channel, "Looking up character")
	with open('data/characters.json') as json_data:
		if len(message.content.split()) < 2:
			yield from client.send_message(message.channel, "Please inclue a character name")
			return

		character_name = message.content.split()[1]
		character_data = json.load(json_data)
		for character in character_data['characters']:
			if character_name == character['name']:
				yield from client.send_message(message.channel, character['title'])

