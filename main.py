from pprint import pprint
from pydoc import describe
from turtle import left
from YT_client import YT_stats
from secret_data import clientId, clientSec, YT_API_KEY, channelID
from spotify_client import SpotifyClient
from print import genreator_print
from helper_func import inputValidation


# Function to validate user's input regarding if they want their playlist public (or not)
yt = YT_stats(YT_API_KEY, channelID)

def main():
    menuItem = {'Description': '01',
                'Transfer From Youtube': '02',
                'Create a playlist': '03' ,
                'Quit Program': '04'}

    genreator_print.print_welcome(31,8)

    user_ID = input('Enter your spotify username to proceed: ')

    spfy = SpotifyClient(clientId, clientSec, user_ID)

    genreator_print.print_menu(menuItem, 31,8)

    # Validating the menu input
    menu_input = ''
    while (menu_input not in menuItem.values()):
        menu_input= input("Enter the number of the option here: ")
        if menu_input in menuItem.values():        
            if (menu_input == '01'):
                pass
                # print description

            elif (menu_input == '02'):
                # print('Transfering from Youtube...')
                channel_id = input("Enter the channel ID: ")
                yt.get_channel_id(channel_id)

            elif(menu_input == '03'):
                # Get all the necessary input for create playlist parameters
                playlistName = input('Name your playlist: ')
                playlistDesc = input('Describe your playlist: ')
                publicValidation = False
                returnedInput = inputValidation.public_input_validation()
                if returnedInput == 'Y':
                    publicValidation = True

                spfy.create_playlist(user_ID, playlistName, playlistDesc, publicValidation, playlistDesc)
                print('creating a playlist...')
            else:
                print('Quiting program. Goodbye!')
                break
        print('Invalid choice, please try again.')
    # If validation is successful, we move onto sub-menus

if __name__ == '__main__':
    main()