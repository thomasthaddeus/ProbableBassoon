#####################################

#####################################
##          TIC TAC TOE            ##
##  by Stephanie Ort, Thad Thomas  ##
##            IS 201               ##
##    Fundamentals of Computing    ##
#####################################

#####################################

from asyncio import __all__
import random
import logging
logging.basicConfig(filename='gamelog.txt',filemode='a',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of Program')
#Constant Variables
BOARD_KEYS = list('123456789')
X, O, BLANK = 'X', 'O', " "


welcome = ("Welcome to Tic Tac Toe\n")
directions = ("""Directions::
                \nuno: Choose your piece: X or O.
                \nThe computer randomly decides who goes uno.
                \nThen pick a move on the board.
                \nUse the numbers 1-9 to pick a move on the board.""")

def main():
    """Main Loop for running our Game"""
    print(welcome, directions)
    bb = blank_board()
    get_piece()
    uno = player_one()
    # true loop of game
    while True:
        print(get_board(bb))
                
        while not empty_space(bb, uno): 
            print('{} Its your turn to play. Choose a move'.format(uno))
            turn = input()
            marker(bb, turn, player)
            i+=1
            
            try:
                input(bb)
            except ValueError:
                raise logging.info()
            else:
                if check_win(bb, player):
                    print(get_board(bb))
                    break
                elif check_tie(bb):
                    print(get_board(bb))
                    break
        if not replay(): 
            break
        else: 
            i = 1
            player = input()
logging.info('End of Program')

def replay():
    playAgain = input("Do you want to play again (Y)es / (N)o ?")
    try:
        if playAgain.upper() == 'Y':
            return True
        elif playAgain.upper() == 'N':
            return False
    except ValueError:
        raise logging.exception
    else: 
        return main()

def get_piece():
    """Defines which piece the user is and whether they go uno or second"""
    piece = ""
    while piece != 'X' and piece != 'O':
        print("To Play Please Select Either X's or O's:  ")
        piece = input().upper()
        try:
            if piece == 'X' :
                return 'X'
            elif piece == 'O':
                return 'O'
        except: 
            print('Please input either X\'s or O\'s')
        else: 
            return piece
 
def player_one():
    if random.choice(0,1)==0:
        return 'computer'
    else:
        return 'player'

def blank_board():
    """Displays a blank bb of the board"""
    blank = {}
    for free_space in BOARD_KEYS:
        blank[free_space]= BLANK
    return blank

def get_board(board):
    '''Displays visual representation  of board'''
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
|______|______|______|
""".format(board['1'],board['2'],board['3'],
           board['4'],board['5'],board['6'],
           board['7'],board['8'],board['9'])

def check_win(board, player):
    '''Checks for winner using the board'''
    i, mark = board, player 
    return ((i['1'] == i['2'] == i['3'] == mark) or  # 1. top_horizon
            (i['4'] == i['5'] == i['6'] == mark) or  # 2. mid_horizon
            (i['7'] == i['8'] == i['9'] == mark) or  # 3. bottom_horizon
            (i['1'] == i['4'] == i['7'] == mark) or  # 4. left_vertical
            (i['2'] == i['5'] == i['8'] == mark) or  # 5. middle_vertical
            (i['3'] == i['6'] == i['9'] == mark) or  # 6. right_vertical
            (i['1'] == i['5'] == i['9'] == mark) or  # 7. tl_br
            (i['3'] == i['5'] == i['7'] == mark))    # 8. tr_bl    

def marker(board, free_space, move):
    """draw on the board"""
    board[free_space] = move

def empty_space(board, free_space):
    '''Check if space is free on the board'''
    return free_space in BOARD_KEYS and board[free_space] == BLANK

def make_move(board, free_space, piece):
    """Makes a move on the board"""
    board[free_space] = piece
    
def check_tie(board):
    '''Checks board for a Tie'''
    logging.info("Checking for a tie")
    for free_space in BOARD_KEYS:
        if board[free_space] == BLANK:
            return False
        else:
            return ("Game is a Tie")

def minimax(board): # still not implemented
    '''criteria for Minimax'''
    
    if check_win == False:
        return -100
    elif check_win == True:
        return 100
    elif check_tie():
        return 0
    
    if max:
        bestScore = -100
        for key in BOARD_KEYS:
            if (board[key] == ''):
                board[key] = False
                score = (board, 0, False)
                return False    
            elif (score > bestScore):
                bestScore = score 
        return bestScore

    else:
        bestScore = 100
        for key in BOARD_KEYS:
            if (board[key] == ''):
                board[key] = True
                score = (board, 0, True)
                if (score < bestScore):
                    bestScore = score
        return bestScore

if __name__ == '__main__':
    main()