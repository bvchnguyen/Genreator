# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class song(object):
    def __init__(self, artist, track):
        self.artist = artist
        self.track = track

class YT_client(object):
    def __init__(self, credentials_locations):
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            credentials_locations, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)
        
        self.YT_client = YT_client
    
    def get_playlist(self):
        request = self.YT_client.playlist().list(
            part = "id, snippet",
            maxResult = 20,
            mine = True
        )
        response = request.execute()

        playlist = [playlist for playlist in response['items']]

        return playlist

    def get_vid_from_pList(self, plist_Id):
        songs = []
        request = self.YT_client.playlistItem().list(
            plist_Id = plist_Id,
            part = "id, snippet",
        )
        response = request.execute()

        for item in response['item']:
            video_Id = item['snippet']['resourceId']['videoId']
            artist, track = self.get_artist_and_track_from_video(video_Id)
            if artist and track:
                songs.append(song(artist,track))

    def get_artist_track_from_vid(self, video_Id):

        YT_url = f'https://www.youtube.com/watch?v={video_Id}'
        vid = youtube_dl.YoutubeDL({'quiet': True}).extract_info(
            
        )