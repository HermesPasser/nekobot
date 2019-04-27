from utils import openJSON
from bot import start

if (__name__ == '__main__'):
	try:
		print('[Nekobot] starting...')
		token = openJSON('credentials.json')['discord_token']
		start(token)
	except (KeyboardInterrupt, SystemExit):
		print('[Nekobot] closing...')
