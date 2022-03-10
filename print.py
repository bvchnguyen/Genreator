class genreator_print(object):
    def __init__(self) -> None:
        pass
    def print_menu(left_w, right_w):
        menuItem = {'Create a playlist': '01', 'Transfer From Youtube': '02' , 'Quit Program': '03'}
        
        print('GENREATOR MENU'.center(left_w + right_w, '-'))
        for k, v in menuItem.items():
            print(k.ljust(left_w, '.') +str(v).rjust(right_w))