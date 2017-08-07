import discord
import asyncio
import subprocess
import aiohttp
import json

from json_utilities import json_from_url

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
				data = yield from json_from_url('http://www.dustloop.com/wiki/api.php?action=query&format=json&prop=images&titles=' + character['title'] + '&imlimit=50')
				page_id = str(list(data['query']['pages'].keys())[0])
				image_data = data['query']['pages'][page_id]['images']

				for image in image_data:
					if 'Portrait' in image['title']:
						yield from client.send_message(message.channel, image['title'])
