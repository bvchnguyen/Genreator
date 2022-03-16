from YT_client import YT_stats
from secret_data import clientId, clientSec, YT_API_KEY, channelID
from spotify_client import SpotifyClient
import requests

sp = SpotifyClient()
yt = YT_stats(YT_API_KEY, channelID)

yt.get_channel_stats()
title_list = yt.get_channel_video_title()
artist, track = yt.split_title(title_list)
sp.search_spotify(artist, track)
# yt.dump()



                











