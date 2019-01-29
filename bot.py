from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import requests
import json
import random
# import playlist

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)
# if token is Null:
# 	print("token")

f= open("./playlist.txt","w+")
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
        f.write(track['name'] + ' - ' + track['artists'][0]['name'] + "\n")
else:
    print ("Can't get token for", username)
f.close()


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Registering the updater and dispatcher
updater = Updater(token='781062472:AAErrpT1ZpRpZKTDetNm3DSDw0l4TLQWbsg')
dispatcher = updater.dispatcher


#For the start command
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi!! I'm Spotibot, please send your Spotify Authentication code")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


def echo(bot, update):
	global bud
	bud = update.message.text
	#print(bud)
	textmess = "Here is your authcode:" + update.message.text
	botmessage=""

	with open('playlist.txt') as f:
		for line in f.readlines():
			print(line+"hiidhfgidufhigdufhgidufhiuh")
			botmessage+=line+"\n"
	bot.send_message(chat_id=update.message.chat_id, text=botmessage )
	bot.send_message(chat_id=update.message.chat_id, text= "Looks like you love Justin Bieber. Might be a great idea to look into some real music!")


	# bot.send_message(chat_id=update.message.chat_id, text=textmess)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def echoPlaylist(bot, update):
	# global bud
	# bud = update.message.text
	#print(bud)
	# textmessage =  update.message.text
	botmessage=""
	with open('playlist.txt') as f:
		for line in f.readlines():
			print(line+"hiidhfgidufhigdufhgidufhiuh")
			botmessage+=line+"\n"
	bot.send_message(chat_id=update.message.chat_id, text=botmessage)
echo_handler2 = MessageHandler(Filters.text, echoPlaylist)
dispatcher.add_handler(echo_handler2)


#For photos
def photo(bot, update):
    file_id = update.message.photo[-1].file_id
    newFile = bot.getFile(file_id)
    newFile.download('test.jpg')
    bot.sendMessage(chat_id=update.message.chat_id, text="Got your picture mate!")
    imagerec(bot, update)

def playlistTransfer(bot, update):
	 f = open('playlist.txt')
	 for line in f:
	 	bot.sendMessage(chat_id=update.message.chat_id, text="Got your picture mate!")
	 f.close()



# #For image classification
# def imagerec(bot, update):
# 	url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"
# 	querystring = {"returnFaceId":"true","returnFaceLandmarks":"false","returnFaceAttributes":"emotion,age,gender"}

# 	image_path = "/Users/AkshayC/Desktop/test.jpg"
# 	image_data = open(image_path, "rb").read()

# 	headers = {
# 		'Ocp-Apim-Subscription-Key': "9495f13ff2764d0f87daec1d820257e8",
# 		'Content-Type': "application/octet-stream",
# 		'cache-control': "no-cache",
# 		'Postman-Token': "67ac9f11-e73a-430f-aca3-eb71b7dcc0a5"
# 		}	

# 	response = requests.request("POST", url, data=image_data, headers=headers, params=querystring)

# 	age = int(response.json()[0]["faceAttributes"]["age"])
# 	emotion = response.json()[0]["faceAttributes"]["emotion"]

# 	maxint = -0.5

# 	for key in emotion:
# 		if (emotion[key] > maxint):
# 			maxint = emotion[key]
# 			emo = key
	
# 	#print(maxint)
# 	print(emo)
# 	#print(age)

# 	print(bud)
# 	classify(bot, update, emo, int(bud))


# photo_handler = MessageHandler(Filters.photo, photo)
# dispatcher.add_handler(photo_handler)

# #For the Location
# def location(bot, update):

# 	locjson = str(str(update.message.location['latitude']) + "," + str(update.message.location['longitude']))
# 	print(locjson)
# 	#bot.sendMessage(chat_id=update.message.chat_id, text=str(update.message.location))
# 	loc(bot, update, locjson)


# location_handler = MessageHandler(Filters.location, location, edited_updates=True)
# dispatcher.add_handler(location_handler)

# #For getting the map link
# def loc(bot, update, locations):

# 	url_pubs = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
# 	params_pubs = {'key' : 'AIzaSyA6zIAya7DpOz8KKAKTr65tw6LNI5ktKzE',
# 	     'location' :  locations,
# 	       'rankby' : 'distance',
# 	        'type'  : 'pub',
# 	     'keyword'  : 'pubs',
# 	     'maxprice' : 3
# 	         }
# 	r = requests.get(url = url_pubs, params = params_pubs)

# 	data = r.json()
# 	restaurant_name = data['results'][0]['name']
# 	lat = data['results'][0]['geometry']['location']['lat']
# 	lng = data['results'][0]['geometry']['location']['lng']
# 	map_url = "maps.google.com/?q="+str(lat)+','+str(lng)
# 	maptext = "Your closest pub is " + restaurant_name + "\n" + map_url

# 	bot.sendMessage(chat_id=update.message.chat_id, text=maptext)


# def classify(bot, update, emo, bud):
# 	with open("alcohols.json") as file:
# 		alcohols = json.load(file)
# 	emotion = emo
# 	budget = bud

# 	#HAPPINESS
# 	if (emotion == "happiness"):
# 		bot.sendMessage(chat_id=update.message.chat_id, text="You seem to be happy! :)")
# 		happinessDrinkDict = {**alcohols['Red Wine'], **alcohols['Beers']}
# 		lst = []
# 		for drink in happinessDrinkDict.keys():
# 			#print(float(happinessDrinkDict[drink]), float(budget))
# 			if float(happinessDrinkDict[drink]) <= float(budget):
# 				lst.append((drink,happinessDrinkDict[drink]))
# 		#print(lst)
# 		happyChoice = lst[random.randint(0,len(lst) - 1)]
# 		finaltext = "Your recommended drink is " + happyChoice[0] + ". The cost of a standard drink is £" + happyChoice[1] + "."
# 		bot.sendMessage(chat_id=update.message.chat_id, text=finaltext)
# 		bot.sendMessage(chat_id=update.message.chat_id, text="Please send your location too!")

