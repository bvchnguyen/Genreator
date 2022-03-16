from pprint import pprint
from pydoc import describe
from turtle import left
from YT_client import YT_stats
from secret_data import clientId, clientSec, YT_API_KEY
from spotify_client import SpotifyClient
from print import genreator_print
# import youtube_dl

yt = YT_stats(YT_API_KEY)

menuItem = {'Description': '01',
            'Transfer From Youtube': '02',
            'Create a playlist': '03' ,
            'Quit Program': '04'}

genreator_print.print_menu(menuItem, 31,8)

menu_input = ''

# Validating the menu input
while (menu_input not in menuItem.values()):
    menu_input= input("Enter the number of the option here: ")
    if menu_input in menuItem.values():        
        break
    print('Invalid choice, please try again.')

# If validation is successful, we move onto sub-menus
if (menu_input == '01'):
    pass
    # print description

elif (menu_input == '02'):
    # print('Transfering from Youtube...')
    channel_id = input("Enter the channel ID: ")
    yt.get_channel_id(channel_id)
    # Pass channel ID to _get_channel_videos
elif(menu_input == '03'):
    print('creating a playlist...')
else:
    print('Quiting program. Goodbye!')
    