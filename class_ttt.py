###################################
#          TIC TAC TOE            #
#  by Stephanie Ort, Thad Thomas  #
#            IS 201               #
#    Fundamentals of Computing    #
###################################

from doctest import debug_script
import random
import logging
logging.basicConfig(filename='ttt_game_log.txt', 
                    filemode='w', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of Program')

#Constant Variables
BOARD_KEYS = list('123456789')
X, O, BLANK = "X", "O", " "

welcome = ("Welcome to Tic Tac Toe\n")
directions = ("""Directions::
                \nFirst: Choose your piece: X or O.
                \nThe computer randomly decides who goes first.
                \nThen pick a spot on the board.
                \nUse the numbers 1-9 to pick a spot on the board.""")

def get_piece():
    """Defines which piece the user is and whether they go first or second"""
    piece = ""
    while not(piece == 'X' or piece == 'O'):
        print("To Play Please Select Either X's or O's:  ")
        piece = input().upper()
        if piece == 'X':
            return ['X', 'O']
        else: 
            return['O','X']
     
def first_player():
    if random.randint(0,1) == 0:
        return('Machine goes first')
    else:
        return('Human goes first')


def main():
    """Main Loop for running our Game"""
    print(welcome, directions)
    copy = blank_board()
    player = print(get_piece())
    turn = first_player()
    playing = True
    # true loop of game
    while playing:
        print(get_board(copy))
        
        while not empty_space(copy, turn): 
            print('{} Its your turn to play. Choose a spot'.format(player))
            turn = input()
        make_move(copy, turn, player)
        
        if check_win(player, copy):
            print(get_board(copy))
            break
        elif minimax(copy):
            print(get_board(copy))
            break
        turn
    return ('would you like to play again')

def get_board(board):
    '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
    return """
 ____________________ 
|      |      |      |
|  {}   |   {}  |   {}  | 1 2 3
|______|______|______|
|      |      |      |
|  {}   |   {}  |   {}  | 4 5 6
|______|______|______|
|      |      |      |
|  {}   |   {}  |   {}  | 7 8 9
|______|______|______|""".format(board['1'],board['2'],board['3'],
                                 board['4'],board['5'],board['6'],
                                 board['7'],board['8'],board['9'])
    

def blank_board():
    """Displays a blank copy of the board"""
    blank = {}
    for i in BOARD_KEYS:
        blank[i]= ' '
    return blank

def make_move(board, move, piece):
    """Displays move"""
    if empty_space(move):
        board[move] = piece
        try:
            minimax
            x = input('Give me a number between 1 and 9: ')
            if x == 'q':
                exit
            x=int(x)
        except ValueError:
            print('Invalid number, Only numbers in empty spaces')
        else:
            if(check_tie()):
                print("Tie Game!")

            elif check_win():
                if piece == 'X':
                    print("Computer wins!")
                    return
                else:
                    print("Player wins!")
                    return
    
def empty_space(board, free_space):
    '''Check if space is free on the board'''
    return free_space in BOARD_KEYS and board[free_space] == BLANK

def check_tie(board):
    '''Checks board for a Tie'''
    logging.info("Checking for a tie")
    for key in board.keys():
        if board[key] == BLANK:
            return False
        else:
            return ("Game is a Tie")

def check_win(board, player):
    '''Checks for winner using the board'''
    i, mark = board, player 
    return(
    (i['1'] == i['2'] == i['3'] == mark) or  # 1. top_horizon
    (i['4'] == i['5'] == i['6'] == mark) or  # 2. mid_horizon
    (i['7'] == i['8'] == i['9'] == mark) or  # 3. bottom_horizon
    (i['1'] == i['4'] == i['7'] == mark) or  # 4. left_vertical
    (i['2'] == i['5'] == i['8'] == mark) or  # 5. middle_vertical
    (i['3'] == i['6'] == i['9'] == mark) or  # 6. right_vertical
    (i['1'] == i['5'] == i['9'] == mark) or  # 7. tl_br
    (i['3'] == i['5'] == i['7'] == mark))    # 8. tr_bl


def minimax(self, max, board, computer, player):
    '''criteria for Minimax'''
    
    if check_win(computer):
        return -100
    elif check_win(player):
        return 100
    elif check_tie():
        return 0
    
    if max:
        bestScore = -100
        for key in board.keys():
            if (board[key] == ''):
                board[key] = computer
                score = (board, 0, False)
                return False    
            elif (score > bestScore):
                bestScore = score 
        return bestScore

    else:
        bestScore = 100
        for key in board.keys():
            if (board[key] == ''):
                board[key] = player
                score = self(board, 0, True)
                if (score < bestScore):
                    bestScore = score
        return bestScore

if __name__ == '__main__':
    logging.debug('End of Program')
    main()