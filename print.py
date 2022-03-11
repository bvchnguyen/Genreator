class genreator_print(object):
    def __init__(self) -> None:
        pass
    
    def print_menu(menuItem, left_w, right_w):

        print('GENREATOR MENU'.center(left_w + right_w, '-'))
        for k, v in menuItem.items():
            print(k.ljust(left_w, '.') +str(v).rjust(right_w))