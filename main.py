from pprint import pprint
from pydoc import describe
from turtle import left
from YT_client import YT_stats
from secret_data import clientId, clientSec, YT_API_KEY, channelID, redirect
from spotify_client import SpotifyClient
from helper_func import genreator_print, inputValidation

def main():
    menuItem = {'Description': '01',
                'Transfer From Youtube': '02',
                'Create a playlist': '03' ,
                'Quit Program': '04'}

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
                # print('Transfering from Youtube...')
                channel_id = input('Enter the channel ID: ')

                # Encapsulate this into a function
                yt = YT_stats(YT_API_KEY, channel_id)
                yt.get_channel_id(channel_id)
                yt.get_channel_stats()
                channel_name = yt.get_channel_name()
                print('Extracting songs from', channel_name + '...')
                title_list = yt.get_channel_video_title()
                filtered_title = yt.filter_name(title_list)
                artist, track = yt.split_title(filtered_title)
                found_song_list, song_uri = spfy.search_track_spotify(artist, track)
                genreator_print.print_list(found_song_list, channel_name, 31, 8)               
                createPlaylist_YN = input('\nMake a new playlist to store the returned items?(Y/N): ')

                if inputValidation.YN_validation(createPlaylist_YN) == True:
                    playlist_id = spfy.create_playlist(user_ID)
                    spfy.add_song_to_playlist(user_ID, playlist_id, song_uri)
                else:
                    print('Adding to most recent')
                yt.get_channel_id(channel_id)

            elif(menu_input == '03'):
                pass
            else:
                print('Quiting program. Goodbye!')
                break
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()