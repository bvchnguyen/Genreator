from cgitb import reset
import requests
import urllib.parse
import json

class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def create_playlist(self, name, description, privacy):
        data = json.dumps({
            "name": name,
            "description": "description",
            "public": privacy
        })
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._pl

    def search_song(self, artist, track):
        query = urllib.parse.quote (f'{artist} {track}')
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