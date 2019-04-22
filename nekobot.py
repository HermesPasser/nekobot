from discord.ext.commands import Bot
from discord import File as dFile
from urllib import request
import json, os

CATS_PROVIDER = 'http://aws.random.cat/meow'
bot = Bot(command_prefix="'")

def get_rand_image_url():
	# get a json from random.cat with a random cat image
	json_text = req.urlopen(CATS_PROVIDER).read().decode('ascii')
	
	# parse the json and get the image url
	return json.loads(json_text)['file']

def download_image(url, name):
	f = open(name, 'wb')
	blob = request.urlopen(url).read()
	f.write(blob)
	f.close()

@bot.command(name='cat')
async def _random_cat(ctx):
	name = 'cat.gif'
	url = get_rand_image_url()
	download_image(url, name)
	await ctx.message.channel.send(file=dFile(name))
	os.remove(name)
	
	# ao invés de baixar a img, passar o link direto
	
@bot.command(name='source')
async def source(ctx):
	await ctx.message.channel.send('https://github.com/HermesPasser/nekobot')

with open('credentials.json') as f:
	txt = f.read()
	token = json.loads(txt)['token']
	bot.run(token)
