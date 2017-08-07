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
				url = 'http://www.dustloop.com/wiki/api.php?action=query&format=json&prop=images&titles=' + character['title'] + '&imlimit=50'
			
			response = yield from aiohttp.request('get', url)
			string = (yield from response.read()).decode('utf-8')
			data = json.loads(string)
			page_id = str(list(data['query']['pages'].keys())[0])
			image_data = data['query']['pages'][page_id]['images']

			for image in image_data:
				if 'Portrait' in image['title']:
					yield from client.send_message(message.channel, image['title'])
