from pprint import pprint
from turtle import left
from print import genreator_print
import youtube_dl

menuItem = {'Create a playlist': '01',
            'Transfer From Youtube': '02' , 
            'Quit Program': '03'}

genreator_print.print_menu(menuItem, 25,6)

menu_input = ''

while (menu_input not in menuItem.values()):
    menu_input= input("Enter the number of the option here: ")
    if menu_input in menuItem.values():
        break
    print('Invalid choice, please try again.')

if (menu_input == '01'):
    print('creating a playlist...')
elif(menu_input == '02'):
    print('Transfer From Youtube')
else:
    print('Quiting program. Goodbye!')
    