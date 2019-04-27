from urllib import request
import json

CATS_PROVIDER = 'http://aws.random.cat/meow'

def get_rand_image_url():
	# get a json from random.cat with a random cat image
	response = request.urlopen(CATS_PROVIDER)
	
	if (response.code != 200):
		return None
	
	json_text = response.read().decode('ascii')
	
	# parse the json and get the image url
	return (json.loads(json_text)['file'], 'cat.gif')

 
