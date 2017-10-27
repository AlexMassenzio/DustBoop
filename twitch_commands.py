import discord
import asyncio
import subprocess
import aiohttp
import json

from json_utilities import json_from_url

@asyncio.coroutine
def get_stream(message, client):

	game_id = message.content.split()[1]
	yield from client.send_message(message.channel, game_id)
	twitch_data = yield from json_from_url('https://api.twitch.tv/helix/streams?game_id=' + game_id)
	yield from client.send_message(message.channel, twitch_data)
	yield from client.send_message(message.channel, twitch_data['data'][0]['title'])