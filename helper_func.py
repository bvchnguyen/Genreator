# Class for input validation
class inputValidation(object):
    def __init__(self) -> None:
        pass
    # Function to validate user's input Y/N
    def YN_validation(YN_inp) -> bool:
        validation = True
        while True:
            if YN_inp in ['y', 'Y']:
                validation = True
            elif YN_inp in ['n', 'N']:
                validation = False
            else:
                print('Invalid choice, please only enter (Y/N)')
                validation = False
        return False

    # Function to validate user's input regarding if they want their playlist public (or not)
    def generate_input_validation() -> str:
        while True:
            playListPublic = input('Generate a playlist?(Y/N):')
            if playListPublic in ['y', 'Y', 'n' , 'N']:
                if playListPublic in ['y', 'Y']:
                    return True
                elif playListPublic in ['n', 'N']:
                    return False
            print('Invalid choice, please only enter Y or N.')
        return playListPublic

# Class for pretty printing
class genreator_print(object):
    def __init__(self) -> None:
        pass

    def print_welcome(left_w, right_w):
        print('WELCOME TO GENREATOR'.center(left_w + right_w, '-'), '\n')
        print('Genreator is a program that allows you\nto transfer a youtube playlist or video\nfrom a channel to your spotify playlist.\n')
        print('-'.center(left_w + right_w, '-'))

    def print_menu(menuItem, left_w, right_w):
        print('MAIN MENU'.center(left_w + right_w, '-'))
        for k, v in menuItem.items():
            print(k.ljust(left_w, '.') +str(v).rjust(right_w))
    
    def print_list(input_list, channelName, left_w, right_w):
        print('FOUND TRACKS'.center(left_w + right_w, '-'))
        # print(f'FOUND TRACKS FROM {channelName}'.center(left_w + right_w, '-'))
        for i in range(len(input_list)):
            if (i < 9):
                print('0' + str(i+1) + '. ' + input_list[i])
            else:
                print(str(i+1) + '. ' + input_list[i])
        print('-'.center(left_w + right_w, '-'))
