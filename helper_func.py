class inputValidation(object):

    def public_input_validation():
        while True:
            playListPublic = input('Make playlist public? (Y/N): ')
            if playListPublic in ['y', 'Y', 'n' , 'N']:
                break
            print('Invalid choice, please only enter (Y/N)')
        return playListPublic