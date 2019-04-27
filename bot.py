from discord.ext.commands import Bot
from discord import File as dFile
from urllib import request
from io import BytesIO
from utils import *

modules = openJSON('sources.json')
bot = Bot(command_prefix="'")

@bot.command(name='source')
async def source(ctx):
	await ctx.message.channel.send('https://github.com/HermesPasser/nekobot')

@bot.command(name='quit')
async def quit(ctx):
	exit(0)

async def _process_image(message, attempts = 1):
	if (attempts == 3):
		# happens if something gone really bad in the _random_cat
		print('[Nekobot] Unable to access the url.')
		return

	content = message.content[1:]
	module = importer(modules[content])
	(url, name) = module.get_rand_image_url() # must return a tuplue (url, filename)

	if (url == None):
		print('[Nekobot] Cannot access {0}, trying again...'.format(url))
		await _random_cat(message, attempts + 1)
		return
		
	bytes = request.urlopen(url).read() # TODO: neeed a .code != 200 here too

	data = BytesIO(bytes)
	await message.channel.send(file=dFile(data, filename = name))	

@bot.event
async def on_message(message):
	global modules
	content = message.content

	# for some reason when it's called it's runs message and ""
	if (len(content) <= 2):
		return
	
	print('[Nekobot] trying run "{0}"'.format(content[1:]))
	
	if (content[0] == "'" and content[1:] in modules):
		await _process_image(message)			
	else:
		await bot.process_commands(message)

def start(token):
	bot.run(token)
