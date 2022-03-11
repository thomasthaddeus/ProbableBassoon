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

BOARD_KEYS = ['123456789']


welcome = ("Welcome to Tic Tac Toe\n")
directions = ("""Directions::
                \nFirst: Choose your piece: X or O.
                \nThe computer randomly decides who goes first.
                \nThen pick a spot on the board.
                \nUse the numbers 1-9 to pick a spot on the board.""")

logging.debug('Pick a puck')    
def get_player(mark, player, computer):
    """Defines which piece the user is and whether they go first or second"""
    mark = ""
    player = p1
    computer = p2
    while mark != 'X' and mark != 'O':
        mark = input("To Play Please Select Either (X)'s or (O)'s: ").capitalize
        if p1 == 'X':
            p2 = 'O'
        else: 
            p1 = 'X'

    if random.randint(0,1) == 0:
        print("{p1} goes first".format(player))
    else:
        print("{p2} goes first".format(computer))
    
    return 

def get_board(board):
    '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
    return """
 ____________________ 
|      |      |      |
|  {}  |  {}  |  {}  | 1 2 3
|______|______|______|
|      |      |      |
|  {}  |  {}  |  {}  | 4 5 6
|______|______|______|
|      |      |      |
|  {}  |  {}  |  {}  | 7 8 9
|______|______|______|""".format(board['1'],board['2'],board['3'],
                                 board['4'],board['5'],board['6'],
                                 board['7'],board['8'],board['9'])
    

def copy_board(board):
    """Displays copy of the board"""
    copy = []
    for i in board:
        copy.append(i)
    return copy

def make_move(board, move, piece):
    """Displays move"""
    if empty_space(move):
        board[move] = piece
        try:
            x = input('Give me a number between 1 and 9: ')
            if x == 'q':
                exit
            x=int(x)
        except ValueError:
            print('Invalid number, Only numbers in empty spaces')
        else:
            if(checkTie()):
                print("Tie Game!")

            elif checkWin():
                if piece == 'X':
                    print("Computer wins!")
                    exit()
                else:
                    print("Player wins!")
                    exit()
    
def empty_space(board, free_space):
    '''Check if space is free on the board'''
    return free_space in BOARD_KEYS & board[free_space] == ' '

def checkTie(board):
    '''Checks board for a Tie'''
    logging.info("Checking for a tie")
    for key in board.keys():
        if board[key] == '':
            return False
        else:
            return "Game is a Tie"

def checkWin(board, player):
    '''Checks for winner using the board'''
    i, mark = board, player 
    return(
    (i[1] == i[2] == i[3] == mark) or  # 1. top_horizon
    (i[4] == i[5] == i[6] == mark) or  # 2. mid_horizon
    (i[7] == i[8] == i[9] == mark) or  # 3. bottom_horizon
    (i[1] == i[4] == i[7] == mark) or  # 4. left_vertical
    (i[2] == i[5] == i[8] == mark) or  # 5. middle_vertical
    (i[3] == i[6] == i[9] == mark) or  # 6. right_vertical
    (i[1] == i[5] == i[9] == mark) or  # 7. tl_br
    (i[3] == i[5] == i[7] == mark))    # 8. tr_bl


def minimax(self, isMax, board, computer, player):
    '''criteria for Minimax'''
    
    if checkWin(computer):
        return -100
    elif checkWin(player):
        return 100
    elif checkTie():
        return 0
    
    if isMax:
        bestScore = -100
        for key in board.keys():
            if (board[key] == ''):
                board[key] = computer
                score = (board, 0, False)
                board[key] = ''
                if (score > bestScore):
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

logging.debug('Start of Program')
def main():
    """Loop for running Game"""
    print(welcome, directions)
    copy = copy_board()
    user = user.get_player()
    print(get_player(copy, user))
    try:
        while True:
            print(get_board(copy))
            get_player()
            turn = None
            while not empty_space(copy, turn): 
                print(' Its your turn to play. Choose a spot')
                turn = input()
            get_board(copy, turn, user)  
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            get_board(copy)
    except SyntaxError:
        logging.debug()
    
            
if __name__ == '__main__':
    main()

logging.debug('End of Program')