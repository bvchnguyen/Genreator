from YT_client import YT_stats
from secret_data import secrets
import requests

data = secrets()
API, channel_id = data.YT_sec_data()

yt = YT_stats(API, channel_id)
# yt.get_channel_stats()
# yt.get_channel_video_title()
# yt.dump()

title_list = ['Yellow Claw presents €URO TRA$H - The Function Feat. Sky Sky (DYSOMIA Remix)',
            'Boombox Cartel - Heart Of Stone (ft. Nevve)',
            'Just A Gent - but i wish',
            'Ricky Remedy - Sometimes (ft.  TITUS)',
            'vowl. - headlock',
            'LISA - MONEY (CBznar Remix)',
            'Adele - Easy On Me (Wazad & Alieah Cover Remix)',
            'Kanye West - Jonah (Juelz Remix)',
            'Trippie Redd - Miss The Rage ft. Playboi Carti (Pozy Remix)',
            'Hermitude - HyperParadise (Tropkillaz Remix)',
            ]


def split_title(list):
    artist = []
    song_name = []
    for title in title_list:
        for i in range(len(title)):
            if title[i] == "-":
                str_artist = title[0:i-1]
                str_song_name = title[i + 2:len(title)]
                artist.append(str_artist)
                song_name.append(str_song_name)
    return artist, song_name

A, B = split_title(title_list)

print("Artist -- ", A)

                











