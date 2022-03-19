"""
Play TicTacToe
"""
#####################################
##          TIC TAC TOE            ##
##  by Stephanie Ort, Thad Thomas  ##
##            IS 201               ##
##    Fundamentals of Computing    ##
#####################################

import logging
import random
from asyncio import __all__

import numpy as np

logging.basicConfig(filename='gamelog.txt',
                    filemode='a',level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of Program')
#Constant Variables
BOARD_KEYS = list('123456789')
X, O, BLANK = "X", "O", " "

W = ("Welcome to Tic Tac Toe\n")
D = ("""Directions::
     \nuno: Choose your move: X or O.
     \nThe computer randomly decides who goes uno.
     \nThen pick a move on the board.
     \nUse the numbers 1-9 to pick a move on the board.""")

def main():
    """Main Loop for running our Game"""
    print(W, D)
    b_b = blank_board()
    p_1, p_2 = "X", "O"
    turn = player_one()

    # true loop of game
    while True:
        print(get_board(b_b))
        move = None
        while not empty_space(b_b, move):
            if turn == p_1:
                print(f"{p_1} Its your turn to play. Choose a move")
                move = input()
                mark_board(b_b,move,p_1)

                if check_win(b_b, p_1):
                    print(get_board(b_b))
                    print('Winner, Winner, chicken dinner')
                    break
                elif check_tie(b_b):
                    print(get_board(b_b))
                    print('Theres only ties in this game')
                    break
                else:
                    turn = p_2

            else:
                move = minimax(b_b, p_2,O)
                mark_board(b_b,move,p_2)
                if check_win(b_b, p_2):
                    print(get_board(b_b))
                    print('you lose')
                    break
                elif check_tie(b_b):
                    print(get_board(b_b))
                    print('Theres only ties in this game')
                    break
                else:
                    turn = p_1
        if not replay():
            print('End of Game')
            break
logging.info('End of Program')

def replay():
    """Asks if you want to replay TicTacToe"""
    play_again = input("Do you want to play again (Y)es / (N)o ?")
    try:
        if play_again.upper() == 'Y':
            return True
        elif play_again.upper() == 'N':
            return False
    except ValueError:
        print("Value Error: ")
    else:
        main()

def get_move():
    """Defines which move the user is and whether they go uno or second"""
    move = ""
    while move != 'X' and move != 'O':
        print("To Play Please Select Either X's or O's:  ")
        move = input().upper()
        try:
            if move == 'X':
                move ='O'
            else:
                move = 'X'
        except ValueError:
            print("Value error")
        else:
            return move

def player_one():
    '''Who goes first'''
    if random.randint(0,1)==0:
        return "O" # Computer
        return "X" # Player

def blank_board():
    """Displays a blank b_b of the board"""
    logging.debug("check the board for blank spot")
    board = {}
    for free_space in BOARD_KEYS:
        board[free_space]= BLANK
    return board

def get_board(board):
    '''Displays visual representation  of board'''
    logging.info("get the board")
    topl,topm,topr = board['1'],board['2'],board['3']
    midl,mid,midr  = board['4'],board['5'],board['6']
    botl,botm,botr = board['7'],board['8'],board['9']
    board = f"""
___________________
|     |     |     |
|  {topl}  |  {topm}  |  {topr}  | 1 2 3
|_____|_____|_____|
|     |     |     |
|  {midl}  |  {mid}  |  {midr}  | 4 5 6
|_____|_____|_____|
|     |     |     |
|  {botl}  |  {botm}  |  {botr}  | 7 8 9
|_____|_____|_____|
"""
    return board


def check_win(board, winner):
    '''Checks for winner using the board'''
    i, mark = board, winner
    return ((i["1"] == i["2"] == i["3"] == mark) or  # 1. top_horizon
            (i["4"] == i["5"] == i["6"] == mark) or  # 2. mid_horizon
            (i["7"] == i["8"] == i["9"] == mark) or  # 3. bottom_horizon
            (i["1"] == i["4"] == i["7"] == mark) or  # 4. left_vertical
            (i["2"] == i["5"] == i["8"] == mark) or  # 5. middle_vertical
            (i["3"] == i["6"] == i["9"] == mark) or  # 6. right_vertical
            (i["1"] == i["5"] == i["9"] == mark) or  # 7. tl_br
            (i["3"] == i["5"] == i["7"] == mark))    # 8. tr_bl

def mark_board(board, free_space, mark):
    """draw on the board"""
    logging.info("Placing Piece on Board on board")
    board[free_space] = mark

def empty_space(board, free_space):
    '''Check if space is free on the board'''
    return free_space in BOARD_KEYS and board[free_space] == BLANK

def make_move(board, free_space, move):
    """Makes a move on the board"""
    logging.info("Making a move on the board")
    board[free_space] = move

def check_tie(board):
    '''Checks board for a Tie'''
    logging.info("Checking for a tie")
    for free_space in BOARD_KEYS:
        if board[free_space] == BLANK:
            return False
        else:
            return "Game is a Tie"

def make_best_move(board,free_space):
    '''Find The best move for the board'''
    best_score = -np.inf
    best_move = None
    for free_space in blank_board():
        mark_board(board, free_space,best_move)
        score = max(False, O, board)
        board.undo()
        if score > best_score:
            best_score = score
            best_move = free_space
    return make_move(board, free_space, best_move)

def minimax(board,winner,mark):
    '''minimax decision tree'''
    game = get_board(board)
    if game is check_tie(board):
        return 0
    elif game is check_win(board,winner):
        return 1 if check_win(board, winner) is max else -1

    score = []
    for mark in game:
        mark_board(blank_board(),mark,O)
        score.append(min(not O, winner))
        board.undo()

    return max(score) if O else min(score)

if __name__ == '__main__':
    main()
