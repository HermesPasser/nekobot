# The Catbot
Send a random image from a specific theme to a discord server.

# Discord commands
``'<trigger>`` get a (preferably) random image from a specified source.   
The default source is *random.cat* and it's triggered by ``'cat`` command. You can see the list of sources on the sources.json.    

``'source`` get the github page of this bot. 

# How add a new source

First you need to append *sources.json* with the command that will trigger the catbot and the module that will be called when someone write the trigger on Discord.

**Note:** do not add the bot suffix (**'**) in the command on *sources.json*.  

```json
{ "trigger": "module_name"}
```

Then you will need to implement the module that will get the random url and it's procedure *get_rand_image_url*,  does not matter how the procedure will get the urls and from where. The module must be inside of the *sources* folder. 

The *get_rand_image_url*  must return a tuple with the random url and the name of the image to be posted on Discord.   

**Note:** you can use *sources/mock.py* as an example.  

```python
def get_rand_image_url():
	# logic that will fetch the images from the internet here
	return (url, name) # tuple to return
```
After follow the steps above the new source will be added, you do not need to edit any from the existing files to make it work, the catbot will automatically verify if a message on Discord matches with the signature on the *sources.json* and call the corresponding module.
