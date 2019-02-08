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
			print(line)
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



ests.request("POST", url, data=image_data, headers=headers, params=querystring)
