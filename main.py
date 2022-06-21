from pprint import pprint
from pydoc import describe
from turtle import left
from YT_client import YT_stats
from secret_data import clientId, clientSec, YT_API_KEY, channelID, redirect
from spotify_client import SpotifyClient
from helper_func import genreator_print, inputValidation

def main():

    yt = YT_stats(YT_API_KEY)

    menuItem = {'Description': '01',
                'Transfer From Youtube': '02',
                'Quit Program': '03'}

    genreator_print.print_welcome(31,8)

    user_ID = input('Enter your spotify username to proceed: ')
    spfy = SpotifyClient(clientId, clientSec)
    spfy.user_validation(user_ID)

    genreator_print.print_menu(menuItem, 31,8)

    # Validating the menu input
    menu_input = ''
    while (menu_input not in menuItem.values()):
        menu_input= input('Enter the number of the option here: ')
        if menu_input in menuItem.values():        
            if (menu_input == '01'):
                pass
                # print description

            elif (menu_input == '02'):
                channel_id = input('Enter the channel ID: ')
                # Encapsulate this into a function
                yt.set_channel_id(channel_id)
                channel_name = yt.get_channel_name()
                print('Extracting songs from', channel_name + '...')
                title_list = yt.get_channel_video_title()
                filtered_title = yt.filter_name(title_list)
                artist, track = yt.split_title(filtered_title)
                found_song_list, song_uri = spfy.search_track_spotify(artist, track)
                genreator_print.print_list(found_song_list, channel_name, 31, 8)               

                if inputValidation.generate_input_validation() == True:
                    playlist_name = channel_name + ' Youtube Transfer'
                    spfy.generate_playlist(playlist_name, user_ID, song_uri)
                else:
                    playlist_id = spfy.create_playlist(user_ID, song_uri)
            elif (menu_input == '03'):
                print('Quiting program. Goodbye!')
                break
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()