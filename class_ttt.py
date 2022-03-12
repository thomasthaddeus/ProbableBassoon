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

def main():
    """Main Loop for running our Game"""
    print(welcome, directions)
    copy = blank_board()
    get_piece()
    first = first_player()
    i = 1
    # true loop of game
    while True:
        first
        print(get_board(copy))
                
        while not empty_space(copy): 
            player=[X,O]
            i = 0
            for i in range(10):
                if i % 2 == 0:
                    player[0]
                else: 
                    player[1]

            print('{} Its your turn to play. Choose a spot'.format(player))
            turn = input()
            marker(copy, turn, player)
            i+=1
            
            if check_win(copy):
                print(get_board(copy))
                break
            elif check_tie(copy):
                print(get_board(copy))
                break
        if not replay(): 
            break
        else: 
            i = 1
            player = input()
logging.debug('End of Program')

def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False

def get_piece():
    """Defines which piece the user is and whether they go first or second"""
    piece = ""
    while piece != 'X' and piece != 'O':
        print("To Play Please Select Either X's or O's:  ")
        piece = input().upper()
        try:
            if piece == 'X':
                return 'X'
            elif piece == 'O': 
                return 'O'
        except ValueError(exception):
            exception = ("Invalid entry please")
            print(exception)
        else: 
            return piece
     
def first_player():
    if random.randint(0,1) == 0:
        return X
    else:
        return O


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
|______|______|______|""".format(board['1'],board['2'],board['3'],
                                 board['4'],board['5'],board['6'],
                                 board['7'],board['8'],board['9'])
    

def blank_board():
    """Displays a blank copy of the board"""
    blank = {}
    for free_space in BOARD_KEYS:
        blank[free_space]= BLANK
    return blank

def make_move(board, free_space, piece):
    """Displays move"""
    if empty_space(free_space, piece):
        board[free_space] = piece
    ''' try:
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
                return '''
    
def empty_space(board, free_space):
    '''Check if space is free on the board'''
    return free_space in BOARD_KEYS and board[free_space] == BLANK

def check_tie(board):
    '''Checks board for a Tie'''
    logging.info("Checking for a tie")
    for free_space in BOARD_KEYS:
        if board[free_space] == BLANK:
            return False
        else:
            return ("Game is a Tie")

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



def minimax(board):
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

def marker(board, free_space, spot):
    """draw on the board"""
    board[free_space] = spot

if __name__ == '__main__':
 
    main()