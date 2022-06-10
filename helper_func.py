# Class for input validation
class inputValidation(object):
    def __init__(self) -> None:
        pass
    # Function to validate user's input Y/N
    def YN_validation(YN_inp):
        while True:
            if YN_inp in ['y', 'Y', 'n' , 'N']:
                break
            print('Invalid choice, please only enter (Y/N)')
    
    # Function to validate user's input regarding if they want their playlist public (or not)
    def public_input_validation():
        while True:
            playListPublic = input('Make playlist public? (Y/N): ')
            if playListPublic in ['y', 'Y', 'n' , 'N']:
                break
            print('Invalid choice, please only enter (Y/N)')
        return playListPublic

# Class for pretty printing
class genreator_print(object):
    def __init__(self) -> None:
        pass

    def print_welcome(left_w, right_w):
        print('WELCOME TO GENREATOR'.center(left_w + right_w, '-'), "\n")
        print("Genreator is a program that allows you\nto transfer a youtube playlist or video\nfrom a channel to your spotify playlist.\n")
        print('-'.center(left_w + right_w, '-'))

    def print_menu(menuItem, left_w, right_w):
        print('MAIN MENU'.center(left_w + right_w, '-'))
        for k, v in menuItem.items():
            print(k.ljust(left_w, '.') +str(v).rjust(right_w))
    
    def print_list(input_list):
        for i in range(len(input_list)):
            if (i < 10):
                print('0', i, '. ', input_list[i])
            else:
                print(i, '. ', input_list[i])