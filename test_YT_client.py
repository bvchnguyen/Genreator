from YT_client import YT_stats
from secret_data import secrets
import requests

API = secrets().api_key
channel_id = secrets().channel_id

url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyAZKUW9_gAGJBhCXFMHaJkyqoDK-RBg72g&channelId=UC65afEgL62PGFWXY7n6CUbA&part=id&order=date&maxResults=10'

yt = YT_stats(API, channel_id)
yt._get_channel_videos_per_page(url)
# yt.get_channel_video_data()

# data = yt.get_channel_stats()
# yt.dump()





