# import sys
# import spotipy
# import spotipy.util as util


# scope = 'user-library-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username", sys.argv[0])
#     sys.exit()

# token = util.prompt_for_user_token(username,scope)


# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print ("Can't get token for", username)

# export SPOTIPY_CLIENT_ID='97d6a59449964fdd920d6bf2a210ed83'
# export SPOTIPY_CLIENT_SECRET='b088d8381d544ebe8b82d3d008ab168e'
# export SPOTIPY_REDIRECT_URI='http://google.com'

# import sys
# import spotipy
# import spotipy.util as util

# def show_tracks(tracks):
#     for i, item in enumerate(tracks['items']):
#         track = item['track']
#         print ("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))


# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         username = sys.argv[1]
#     else:
#         print ("Whoops, need your username!")
#         print ("usage: python user_playlists.py [username]")
#         sys.exit()

#     token = util.prompt_for_user_token(username)
#     print('bye')
#     if token:
#         sp = spotipy.Spotify(auth=token)
#         playlists = sp.user_playlists(username)
#         for playlist in playlists['items']:
#             if playlist['owner']['id'] == username:
#                 print()
#                 print (playlist['name'])
#                 print ('  total tracks', playlist['tracks']['total'])
#                 results = sp.user_playlist(username, playlist['id'],
#                     fields="tracks,next")
#                 tracks = results['tracks']
#                 show_tracks(tracks)
#                 while tracks['next']:
#                     tracks = sp.next(tracks)
#                     show_tracks(tracks)
#     else:
#         print ("Can't get token for", username)

# import pprint
# import sys

# import spotipy
# import spotipy.util as util
# import simplejson as json

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

# scope = 'user-top-read'
# token = util.prompt_for_user_token(username, scope)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     ranges = ['short_term', 'medium_term', 'long_term']
#     for range in ranges:
#         print ("range:", range)
#         results = sp.current_user_top_artists(time_range=range, limit=50)
#         for i, item in enumerate(results['items']):
#             print (i, item['name'])
#         print()
# else:
#     print("Can't get token for", username)


  #shows a user's saved tracks (need to be authenticated via oauth)

# import sys
# import spotipy
# import spotipy.util as util

# scope = 'user-library-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

# token = util.prompt_for_user_token(username, scope)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)

# import sys
# import spotipy
# import spotipy.util as util

# scope = 'user-library-read'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print ("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

# token = util.prompt_for_user_token(username, scope)
# # if token is Null:
# # 	print("token")

# f= open("./playlist.txt","w+")
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print (track['name'] + ' - ' + track['artists'][0]['name'])
#         f.write(track['name'] + ' - ' + track['artists'][0]['name'] + "\n")
# else:
#     print ("Can't get token for", username)



# Add tracks to 'Your Collection' of saved tracks

import pprint
import sys
import os
from json.decoder import JSONDecodeError
import spotipy
import spotipy.util as util

scope = 'user-library-modify'

if len(sys.argv) > 2:
    username = sys.argv[1]
    aids = sys.argv[2:]
else:
    print("Usage: %s username album-id ..." % (sys.argv[0],))
    sys.exit()
try:
    token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_saved_albums_add(albums=aids)
    pprint.pprint(results)
    print(type(results))
else:
    print("Can't get token for", username)

