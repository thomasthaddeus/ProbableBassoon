#####################################

#####################################
##          TIC TAC TOE            ##
##  by Stephanie Ort, Thad Thomas  ##
##            IS 201               ##
##    Fundamentals of Computing    ##
#####################################

#####################################
import random 
import logging
logging.basicConfig(filename='gamelog.txt',filemode='a',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of Program')
BOARD_KEYS = list('123456789')
X, O, BLANK = 'X', 'O', " "

tttBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def get_board(board):
    '''Displays visual representation  of board'''
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

#Welcome and begin
print("Welcome to Tic Tac Toe")
print("Enter 'q' to quit at anytime!\n")

def get_piece():
    """Defines which piece the user is and whether they go first or second"""
    while True:
        piece = input("To Play Please Select Either X's or O's:  ").upper()
        if piece == 'X':
            print('You go first!')
            return 'X', 'O'
        elif piece == 'O':
            print('Computer goes first!')
            return 'O','X'
        else: 
            print('x or o?')

#Places X's or O's on the board 
for i in range(9):
    get_board(tttBoard)
    print('Choose a spot 1-9:')
    move = input()
    tttBoard[move] = get_piece()
    if get_piece == 'X':
        get_piece = 'O'
    else:
        get_piece = 'X' 

def player_one(computer, player):
    '''Who goes first'''
    if random.randint(0,1)==0:
        return computer
    else:
        return player

# Best_Moves = [5,1,7,3,2,9,8,6,4]

def marker(board, free_space, move):
    """draw on the board"""
    board[free_space] = move

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

def empty_space(board, free_space):
    '''Check if space is free on the board'''
    return free_space in BOARD_KEYS and board[free_space] == BLANK

def check_tie(board):
    '''Checks board for a Tie'''
    #logging.info("Checking for a tie")
    for free_space in BOARD_KEYS:
        if board[free_space] == BLANK:
            return False
        else:
            return ("Game is a Tie")

def main():
    """Main Loop for running our Game"""
    get_piece(player)
    uno = player_one(player)
    # true loop of game
    while True:
        print(get_board(tttBoard))

        while not empty_space(tttBoard):
            print("{} Its your turn to play. Choose a move".format("X"))
            turn = input()
            marker(tttBoard, turn, player)
            # i += 1

            try:
                input(tttBoard)
            except ValueError:
                logging.info("Information is")
            else:
                if check_win(tttBoard, player):
                    print(get_board(tttBoard))
                    break
                elif check_tie(tttBoard):
                    print(get_board(tttBoard))
                    break
        if not replay(): 
            break
        else: 
            # i = 1
            player = input()
logging.info('End of Program')

def replay():
    playAgain = input("Do you want to play again (Y)es / (N)o ?")
    """Asks if you want to replay TicTacToe"""
    try:
        if playAgain.upper() == 'Y':
            return True
        elif playAgain.upper() == 'N':
            return False
    except ValueError:
        raise logging.exception
        print("Value Error: ")
    else: 
        return main()
    

get_board(tttBoard)  

