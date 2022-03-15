from cgitb import reset
from spotipy.oauth2 import SpotifyClientCredentials
from secret_data import clientId, clientSec
import spotipy
import spotipy.util as util
import requests
import urllib.parse
import json

class SpotifyClient(object):

    def test_spotipy(self):

        birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=clientId, client_secret=clientSec
        ))

        results = spotify.artist_albums(birdy_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = spotify.next(results)
            albums.extend(results['items'])

        for album in albums:
            print(album['name'])
    
    # def __init__(self, api_token):
    #     self.api_token = api_token

    def test_search(self, artist_list, title_list):

        # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=clientId, client_secret=clientSec
        ))
        for i in range(len(artist_list)):
            artist = artist_list[i]
            track_name = title_list[i]
            results = spotify.search(q="artist:" + artist + " track:" + track_name, type="track")
            if results == None: 
                print("cannot find " + artist + track_name)
            else:
                print("found " + artist + track_name)  

    def create_playlist(self, name, description):
        # Function to create a playlist based on user's input
        # Get the name and the description in main
        # Add them to json data
        data = json.dumps({
            "name": name,
            "description": description
        })
        # API url
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._pl

    def search_song(self, artist, track):
        # Function to search the song by the artist and name
        query = urllib.parse.quote (f'{artist} {track}')
        # https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20
        url_query = f'https://api.spotify.com/v1/search?q={query}&type=track'
        response = requests.get(
            url_query,
            headers={
                "Content-type": "application/json",
                "Authorization": f'Bearer {self.api_token}'
            }
        )
        response_json = response.json()
        results = response_json['track']['items']
        if results:
            return results[0]['id']
        else:
            raise Exception(f'No song found under this {artist}')
    
    def add_song_to_playlist(self, song_id):
        url = 'https://api.spotify.com/v1/me/tracks'
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-type": "application/json",
                "Authorization": f'Bearer {self.api_token}'
            }
        )
        return response.ok