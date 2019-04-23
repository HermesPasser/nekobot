from discord.ext.commands import Bot
from discord import File as dFile
from urllib import request
import json, io

CATS_PROVIDER = 'http://aws.random.cat/meow'
bot = Bot(command_prefix="'")

def get_rand_image_url():
	# get a json from random.cat with a random cat image
	response = request.urlopen(CATS_PROVIDER)
	
	if (response.code != 200):
		return None
	
	json_text = response.read().decode('ascii')
	
	# parse the json and get the image url
	return json.loads(json_text)['file']

@bot.command(name='cat')
async def _random_cat(ctx, attempts = 1):
	# something gone really bad in the cats_privider
	if (attempts == 3):
		print('[Nekobot] Unable to access the url.')
		return
	
	name = 'cat.gif'
	url = get_rand_image_url()
	
	if (url == None):
		print('[Nekobot] Cannot access {0}, trying again...'.format(url))
		await _random_cat(ctx, attempts + 1)
		return
	
	bytes = request.urlopen(url).read() # TODO: neeed a .code != 200 here too

	data = io.BytesIO(bytes)
	await ctx.message.channel.send(file=dFile(data, filename = name))
	
	
@bot.command(name='source')
async def source(ctx):
	await ctx.message.channel.send('https://github.com/HermesPasser/nekobot')

if (__name__ == '__main__'):
	try:
		with open('credentials.json') as f:
			print('[Nekobot] starting...')
			txt = f.read()
			token = json.loads(txt)['discord_token']
			bot.run(token)
	except KeyboardInterrupt:
		print('[Nekobot] closing...')
