from cgitb import reset
from spotipy.oauth2 import SpotifyClientCredentials
from secret_data import clientId, clientSec
import spotipy
import spotipy.util as util
import requests
import urllib.parse
import json

# Spotipy documentation -- https://spotipy.readthedocs.io/en/2.19.0/#

class SpotifyClient(object):

    def search_spotify(self, artist_list, title_list):
        # Function to search spotify using spotipy by using the artist and title list that we've returned in YT_client
        
        # Initalizing and verifying our spotify credentials
        # May move this to _init_, but for now, keeping this here for further testing
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=clientId, client_secret=clientSec
        ))
        # Loop through our artist & Title list
        for i in range(len(artist_list)):
            artist = artist_list[i]
            track_name = title_list[i]
            # Call the spotipy search function and pass through the given parameters
            # For our case, we want just the top result found when searching, thus, limit = 1
            # Result will return with json data regarding what's found
            results = spotify.search(q="artist:" + artist + " track:" + track_name, limit=1, type="track")
            print(results)

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