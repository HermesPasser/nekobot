
def importer(module):
	"""Load a submodule from sources"""
	from importlib import import_module
	return import_module('sources.{0}'.format(module))
	
def openJSON(text):
	"""Open a file and parse its JSON"""
	import json
	with open(text) as f:
		obj = json.loads(f.read())
	return obj
