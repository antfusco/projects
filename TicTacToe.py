
def display_board(board):
    print('     |   |      ')
    print(f'  {board[7]}  | {board[8]} |  {board[9]}   ')
    print('     |   |      ')
    print('---------------')
    print('     |   |      ')
    print(f'  {board[4]}  | {board[5]} |  {board[6]}  ')
    print('     |   |      ')
    print('---------------')
    print('     |   |      ')
    print(f'  {board[1]}  | {board[2]} |  {board[3]}  ')
    print('     |   |      ')


def player_input():
    dic = {'player1': ' ', 'player2': ' '}
    while dic['player1'] not in ['X', 'O']:
        dic['player1'] = input('Please pick X or O: ')
        if dic['player1'] not in ['X', 'O']:
            print('I said pick X or O...')
    if dic['player1'] == 'X':
        dic['player2'] = 'O'
    else:
        dic['player2'] = 'X'
    return dic


def place_marker(board, marker, position):
    board[position] = marker
    return board[position]

def win_check(board, mark):
    #check horizontal
    mylist = [mark]*3
    if mylist == [board[7],board[8],board[9]] or mylist == [board[4],board[5],board[6]] or mylist ==[board[1],board[2],board[3]]:
        return True
    #check vertical
    if mylist == [board[1],board[4],board[7]] or mylist == [board[8],board[5],board[2]] or mylist == [board[3],board[6],board[9]]:
        return True
    #check diagonal
    if mylist == [board[1],board[5],board[9]] or mylist == [board[7],board[5],board[3]]:
        return True
    else:
        return False

import random

def choose_first():
    x = random.randint(1,2)
    print(f'Player {x}, shall we get started?')

def space_check(board, position):
    if board[position] not in ['X','O']:
        return True
    else:
        return False

def full_board_check(board):
    mycheck = set(board[1:])
    if mycheck == {'X','O'}:
        return True
    else:
        return False


def player_choice(board):
    position = 0
    while position not in list(range(1, 10)) or not space_check(board, position):
        position = int(input('Pick your position 1-9 '))

    return position


def replay():
    again = 'WRONG'
    while again not in ['Y', 'N','y','n']:
        again = input("Wanna play? (Y/N) ")
        if again not in ['Y', 'N','y','n']:
            print("invalid entry")
        elif again == 'Y' or again == 'y':
            return True
        else:
            return False


print('Welcome to Tic Tac Toe!')

while replay():
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    choose_first()
    dic = player_input()
    display_board(board)
    # while True:
    # Set the game up here
    # pass

    while not win_check(board, dic['player1']) and not win_check(board, dic['player2']) and not full_board_check(board):
        place_marker(board, dic['player1'], player_choice(board))
        print('\n' * 100)
        display_board(board)
        if win_check(board, dic['player1']):
            print(f"Three {dic['player1']} in a row! good job!")
            break
        if full_board_check(board):
            print("It's a tie!")
            break
        place_marker(board, dic['player2'], player_choice(board))
        print('\n' * 100)
        display_board(board)
        if win_check(board, dic['player2']):
            print(f"Three {dic['player2']} in a row! good job!")
            break
        if full_board_check(board):
            print("It's a tie!")
            break
