from cgitb import reset
from secret_data import clientId, clientSec, redirect, YT_API_KEY
from spotipy.oauth2 import SpotifyOAuth
from helper_func import inputValidation
from YT_client import YT_stats
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
        self.track_uri = None

    def spfy_spotipy(self):
        spOAuth_ob = spotipy.SpotifyOAuth(client_id=clientId,
                                        client_secret=clientSec,
                                        redirect_uri=redirect,
                                        scope='playlist-modify-public')

        token_data = spOAuth_ob.get_access_token()
        token = token_data['access_token']

        spotipy_ob = spotipy.Spotify(auth=token)
        self.spotipy_lib = spotipy_ob
        return spotipy_ob
        # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        #                        client_id=clientId, client_secret=clientSec))
        
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
        found_track = [] # for display
        track_uri_list = [] # for adding via spotipy
        for i in range(len(artist_list)):
            artist = artist_list[i]
            track_name = title_list[i]
            # Call the spotipy search function and pass through the given parameters
            results = self.spfy_spotipy().search(q='artist:' + artist + ' track:' + track_name, limit=1, type='track')
            if ((results['tracks']['total']) != 0):
                track = results['tracks']['items'][0]['artists'][0]['name'] + ' - ' + results['tracks']['items'][0]['name']
                song_uri = results['tracks']['items'][0]['uri']
                found_track.append(track)
                track_uri_list.append(song_uri)
        return found_track, track_uri_list

    def create_playlist(self, user_id) -> str:
        # Function to create a playlist based on user's input
        playlistName = input('Name your playlist: ')
        playlistDesc = input('Describe your playlist: ')

        playlist = self.spfy_spotipy().user_playlist_create(user = user_id, name = playlistName, public=True, 
                                    collaborative=False, description=playlistDesc)

        return playlist['id']

    def get_user_playlist(self):
        user_playlists = self.spfy_spotipy().current_user_playlists(limit=15, offset=0)
        print(user_playlists)

    def generate_playlist(self, playlistName, user_id, track_uri):
        
        user_playlists = self.spfy_spotipy().current_user_playlists(limit=15, offset=0)
    
        yt = YT_stats(YT_API_KEY)

        if playlistName in user_playlists:
            self.spfy_spotipy().user_playlist_add_tracks(user = user_id, 
                                            playlist_id = playlist['items'][0]['id'], 
                                            tracks = track_uri, 
                                            position=None)
            return
        else:
            playlist = self.spfy_spotipy().user_playlist_create(user = user_id, name = playlistName, public=True, 
                                        collaborative=False, description='Transfered from Youtube')
            
            self.spfy_spotipy().user_playlist_add_tracks(user = user_id, 
                                                        playlist_id = playlist['id'], 
                                                        tracks = track_uri, 
                                                        position=None)

    def add_song_to_playlist(self, ID, playlistID, track_uri):
        added = self.spfy_spotipy().user_playlist_add_tracks(user = ID, 
                                                    playlist_id = playlistID, 
                                                    tracks = track_uri, 
                                                    position=None)
        