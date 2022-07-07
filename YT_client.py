import dataclasses
import json
from turtle import update
from weakref import KeyedRef
import youtube_dl
import requests
import json
import pprint
import re

class YT_stats(object):
    
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.channel_id = None
        self.channel_statistics = None
        self.channel_name = None
        self.video_data = None
        self.video_title = None

    def set_channel_id(self, input):
        # Function to set channel ID
        self.channel_id = input
        return self.channel_id

    def get_channel_title(self, video_id, part) -> dict:
        url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}'

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0]['snippet']['channelTitle']
        except:
            print('No such data exists')
            data = dict()
        # print(data)
        return data

    def get_channel_name(self) -> str:
        # Get the json data through _get_channel_videos function
        name = []
        channel_videos = self.get_channel_videos(limit=1)
        # We loop through to channel_videos to get the title
        for video_id in channel_videos:
            data = self.get_channel_title(video_id, 'snippet')
            # Append the returned data (In this case, the title string)
            name.append(data)
        self.channel_name = name[0]
        return name[0]

    def get_channel_video_title(self) -> list:
        # Function to get the title of from the json data
        title = []
        # Get the json data through _get_channel_videos function
        channel_videos = self.get_channel_videos(limit=5)

        # We loop through to channel_videos to get the title
        for video_id in channel_videos:
            data = self.get_single_video_title(video_id, 'snippet')
            # Append the returned data (In this case, the title string)
            title.append(data)
        # print(title)
        # Assign the list to the video_data object
        self.video_title = title
        return title

    def get_single_video_title(self, video_id, part) -> dict:
        url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}'

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        # print(data)
        try:
            data = data['items'][0]['snippet']['title']
        except:
            print('Error')
            data = dict()
        return data

    def filter_name(self, song_name) -> list:
        # Function to filter the name of the song using REGEX
        # If the name includes things such as (lyrics), (official music video), etc
        # This helps filter the name so that it's easier to search in spotify
        updated_name = []
        temp = ''
        for song in song_name:
            temp = re.sub(r'[\(\[].*?[\)\]]', '', song)
            updated_name.append(temp)
        return updated_name

    def split_title(self, title_list) -> list:
        # Function to split the title between the artist and song
        # In most format on youtube, the title consists of Artist - Song Name
        # Here, we will consider the featuring artist to be a part of the song name for simplicity
        artist = []
        song_name = []
        # Loop through the title list
        for title in title_list: 
            # Loop through each title string
            for i in range(len(title)):
                # Once we find the delimiter "-", we can slice the string into two
                if title[i] == '-':
                    # Artist is anything before the delimiter
                    str_artist = title[0:i-1]
                    # Song title is anything after the delimiter
                    str_song_name = title[i + 2:len(title)]
                    # Append them to the corresponding list
                    artist.append(str_artist)
                    song_name.append(str_song_name)
        song_name = self.filter_name(song_name)
        return artist, song_name

    def get_channel_videos(self, limit = None) -> dict:

        # Function to get the n most recent videos of the given channel

        # Get the URL from google API and pass it as an f string to URL variable
        # We passed in the channel_ID and api_key in the query slots
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        # We check to see if limit is not None, and that it is in instance of an int datatype
        if limit is not None and isinstance(limit, int):
            # If conditions are true, we append our desired max result into the url string
            url += '&maxResults=' + str(limit)
        # This block is primarily use for if you have 50+ returned results
        vid, npt = self.get_channel_videos_per_page(url)
        # index variable
        i = 0
        while(npt is not None and i < 1):
            # We append the page token query into the url
            next_url = url + '&pageToken=' + npt
            # Pass it to the per page helper function
            next_vid, npt = self.get_channel_videos_per_page(next_url)
            # Update the dictionary if the key does not exists in it
            vid.update(next_vid)
            # Increment our index
            i += 1

        return vid

    def get_channel_videos_per_page(self, url) -> dict:

        # This function is only useful if your desired max result is over 50,
        # which the returned results will be stored into multiple pages
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        if 'items' not in data:
            print('not found')
            return channel_videos, None
        item_data = data['items']
        nextPageToken = data.get('nextPageToken', None)
        for item in item_data: 
            try: 
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print('No video found.')
        
        return channel_videos, nextPageToken
