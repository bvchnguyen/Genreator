class genreator_print(object):
    def __init__(self) -> None:
        pass

    def print_menu(menuItem, left_w, right_w):
        print('WELCOME TO GENREATOR'.center(left_w + right_w, '-'), "\n")
        print("Genreator is a program that allows you\nto transfer a youtube playlist or video\nfrom a channel to your spotify playlist.\n")
        print('MENU'.center(left_w + right_w, '-'))
        for k, v in menuItem.items():
            print(k.ljust(left_w, '.') +str(v).rjust(right_w))
