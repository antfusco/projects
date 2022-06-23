def display(gamelist):
    print(gamelist)
def input_pos():
    value = 'wrong'
    while value not in ['0','1','2']:
        value = input('Enter a value, (0-2): ')
        if value not in ['0','1','2']:
            print('try again')
    return int(value)


def change_it(position):
    gamelist[position] = input('what do you want to change it to? ')
    return gamelist
def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input('You wanna keep going? (Y or N): ')
        if choice not in ['Y','N','y','n']:
            print('Invalid entry')
        elif choice == 'Y' or choice == 'y':
            return True
        else:
            return False


gameon = True
gamelist = [0,1,2]
while gameon == True:
    display(gamelist)
    change_it(input_pos())
    display(gamelist)
    gameon = gameon_choice()
