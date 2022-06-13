from pprint import pp, pprint
from turtle import title
from YT_client import YT_stats
from secret_data import clientId, clientSec, YT_API_KEY, channelID
from spotify_client import SpotifyClient
import requests

spfy = SpotifyClient(clientId, clientSec)
yt = YT_stats(YT_API_KEY, channelID)

def test_YT():
    yt.get_channel_stats()
    yt.get_channel_name()
    # title_list = yt.get_channel_video_title()
    # filtered_title = yt.filter_name(title_list)
    # # artist, track = yt.split_title(title_list)

    # # print(title_list)
    # pprint(filtered_title)
    # sp.search_spotify(artist, track)

    # yt.dump()

def main():
    channelList = ['Besomorph, 2Scratch & M.I.M.E - Blessed ',
                    'DaWave & Monkid - Energy',
                    'Hensonn - Sahara ',
                    'Ivy Lab - Double Blind',
                    'Layto - S.O.A.G.',
                    'Tommygunnz x Brxly x N.E.B. - Too Much',
                    'CryJaxx - Lollipop ',
                    'Tiësto & Ava Max - The Motto ',
                    'YehMe2 - Dog Eat Dog ']

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

    
    test_YT()
    # yt.get_channel_name()

    # filtered_title = yt.filter_name(title_list)
    # artist, track = yt.split_title(filtered_title)

    # pprint(filtered_title)
    # pprint(artist)
    # pprint(track)

    # print('Tracks found:', spfy.search_track_spotify(artist, track))

    spotify_username = 'fdjahklfdalk'
    # spfy.user_validation(spotify_username)

if __name__ == '__main__':
    main()


                











