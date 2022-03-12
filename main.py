from pprint import pprint
from turtle import left
from print import genreator_print
import youtube_dl

menuItem = {'Transfer From Youtube': '01',
            'Create a playlist': '02' , 
            'Quit Program': '03'}

genreator_print.print_menu(menuItem, 25,6)

menu_input = ''

# Validating the menu input
while (menu_input not in menuItem.values()):
    menu_input= input("Enter the number of the option here: ")
    if menu_input in menuItem.values():        
        break
    print('Invalid choice, please try again.')

# If validation is successful, we move onto sub-menus
if (menu_input == '01'):
    # print('Transfering from Youtube...')
    input("Enter the channel ID: ")

    # Pass channel ID to _get_channel_videos

elif(menu_input == '02'):
    print('creating a playlist...')
else:
    print('Quiting program. Goodbye!')
    