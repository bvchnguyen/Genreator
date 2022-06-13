from cgitb import reset
from spotipy.oauth2 import SpotifyClientCredentials
from secret_data import clientId, clientSec
from helper_func import inputValidation
import spotipy
import spotipy.util as util
import requests
import urllib.parse
import pprint
import json

# Spotipy documentation -- https://spotipy.readthedocs.io/en/2.19.0/#

class SpotifyClient(object):

    def __init__(self, clientId, clientSec):
        self.client_ID = clientId
        self.client_Secret = clientSec
        self.user_id = None
        self.spotipy_lib = None

    def spfy_spotipy(self):
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
                               client_id=clientId, client_secret=clientSec))

        self.spotipy_lib = spotify
        return spotify
        
    def user_validation(self, user_name) -> bool:
        try:
            self.spfy_spotipy().user(user_name)
            print(f'Access granted: Welcome {user_name}')
            self.user_id = user_name
            return True
        # Have to fix exception catch
        except:
            print(f'No user found under the name {user_name}')
        return False

    def search_track_spotify(self, artist_list, title_list) -> list:
        # Function to search spotify using spotipy by using the artist and title list that we've returned in YT_client
        found_track = []
        for i in range(len(artist_list)):
            artist = artist_list[i]
            track_name = title_list[i]
            # Call the spotipy search function and pass through the given parameters
            results = self.spfy_spotipy().search(q='artist:' + artist + ' track:' + track_name, limit=1, type='track')
            if ((results['tracks']['total']) != 0):
                track = results['tracks']['items'][0]['artists'][0]['name'] + ' - ' + results['tracks']['items'][0]['name']
                found_track.append(track)
        return found_track

    def create_playlist(self, user_id):
        # Function to create a playlist based on user's input
        playlistName = input('Name your playlist: ')
        playlistDesc = input('Describe your playlist: ')
        publicValidation = False
        returnedInput = inputValidation.public_input_validation()
        if returnedInput == 'Y':
            publicValidation = True

        spotipy.user_playlist_create(user = user_id, name = playlistName, public=publicValidation, 
                                    collaborative=False, description=playlistDesc)
    
    def add_song_to_playlist(self, song_id):
        pass