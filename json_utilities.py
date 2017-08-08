import asyncio
import aiohttp
import json

@asyncio.coroutine
def json_from_url(url):
	print('JSON REQUEST: ' + url)
	response = yield from aiohttp.request('get', url)
	string = (yield from response.read()).decode('utf-8')
	return json.loads(string)
