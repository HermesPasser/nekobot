from bot import start
from os import getenv

if (__name__ == '__main__'):
	try:
		print('[Nekobot] starting...')
		token = getenv('DISCORD_TOKEN')
		start(token)
	except (KeyboardInterrupt, SystemExit):
		print('[Nekobot] closing...')
