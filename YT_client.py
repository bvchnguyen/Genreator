import json
from weakref import KeyedRef
import youtube_dl
import requests
import json
import pprint

class YT_stats:
    
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_channel_stats(self):

        # Get the URL from google API and pass it as an f string to URL variable
        # We passed in the channel_ID and api_key in the query slots
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        
        # pass a requests to the URL declared
        json_url = requests.get(url)

        # Load the json data as a text file
        data = json.loads(json_url.text)
        # Grabing the first item in the items list of our loaded json file
        # Then grab the "statistics" value of that first item
        try:
            data = data["items"][0]["statistics"]
        
        # If failed to load, return None
        except KeyError:
            data = None
        
        # Assign our channel_statistics object to the data found
        self.channel_statistics = data
        print(self.channel_statistics)
        return data
    
    def get_channel_video_data(self):
        channel_videos = self._get_channel_videos(limit=10)
        print(channel_videos)
        print(len(channel_videos))

        # parts = ["snippets", "statistics", "contentDetails"]
        # for video_id in channel_videos:
        #     for part in parts:
        #         data = self._get_single_video_data(video_id, part)
        #         channel_videos[video_id].update(data)

        # self.video_data = channel_videos
        # return channel_videos
    

    def _get_single_video_data(self, video_id, part):
        url = f'https://www.googleapis.com/youtube/v3/video?part={part}&id={video_id}&key={self.api_key}'

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except:
            print('Error')
            data = dict()

        return data

    def _get_channel_videos(self, limit = None):

        # Function to get the n most recent videos of the given channel

        # Get the URL from google API and pass it as an f string to URL variable
        # We passed in the channel_ID and api_key in the query slots
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        
        # We check to see if limit is not None, and that it is in instance of an int datatype
        if limit is not None and isinstance(limit, int):
            
            # If conditions are true, we append our desired max result into the url string
            url += '&maxResults=' + str(limit)
        
        # This block is primarily use for if you have 50+ returned results
        # Which would result in the data being stored on multiple json pages
        # We call our per page helper function and pass through the url
        vid, npt = self._get_channel_videos_per_page(url)
        # index variable
        i = 0
        # While loop to run through the number of next pages available
        # We want it to run no more than 10 times per call since 
        # we only have a limited API calls per day

        while(npt is not None and i < 2):

            # We append the page token query into the url
            next_url = url + '&pageToken=' + npt
            
            # Pass it to the per page helper function
            next_vid, npt = self._get_channel_videos_per_page(next_url)

            # Update the dictionary if the key does not exists in it
            vid.update(next_vid)

            # Increment our index
            i += 1

        return vid

    def _get_channel_videos_per_page(self, url):

        # This function is only useful if your desired max result is over 50,
        # which the returned results will be stored into multiple pages

        json_url = requests.get(url)
        data = json.loads(json_url.text)
        print(data)

        # Declare a dictionary for channel videos
        channel_videos = dict()

        # If there are no items in the json file we just parsed, then we return function
        if 'items' not in data:
            print('not found')
            return channel_videos, None

        # Here, we are looping through each pages of json file given for that channel
        item_data = data['items']

        # Get the nextPageToken, or return None if there is none
        nextPageToken = data.get('nextPageToken', None)
        print(nextPageToken)
        for item in item_data: 
            try: 
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print("No video found.")
        

        return channel_videos, nextPageToken

    def dump(self):

        # Create a json file in our directory so we don't have to open it as a link

        # If get_channel_stats returned channel_statistics object as none, we exit function
        if self.channel_statistics is None:
            print('No data is found')
            return
        # fused_data = {self.channel_id: {'channel_statistics': self.channel_statistics,
        #                                 'video_data': self.video_data}}

        # channel_title = self.video_data.popitem()[1].get('channelTitle', self.channel_id)
        channel_title = "Trap City"

        # Replace any whitespace in filename with underscore (and lowercase it)
        channel_title = channel_title.replace(" ", "_").lower()

        # Assign the file as a json file
        file_name = channel_title + '.json'
        
        # Open the file as write-able
        with open(file_name, 'w') as f:
            json.dump(self.channel_statistics, f, indent = 4)
