from argparse import Namespace


Namespace

# place all imports at the top of the file here
import logging
import random
logging.basicConfig(filename='ttt_game_log.txt', 
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# TODO: write coin flip to decide who goes first


class TicTacToe:
    '''Class for playing tic tac toe'''
    welcome = '''Welcome to Tic Tac Toe.\n 
                Our Version by Steph & Thad\n
                To Play Please Select either (X)'s or (O)'s.\n'''

    print(welcome)
    
    def __init__(self, player, computer):
        '''defines the player and their choice of X || O'''
        self.boardSpot = ['1','2','3','4','5','6','7','8','9'] 
        self.player = player
        self.computer = computer

    # Part 5
    # prints the board
    # 5,1,3,7,9,2,4,6,8    
    def getBoard(board):
        '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
        board['a1':'1', 'b1':'2', 'c1':'3',
              'a2':'4', 'b2':'5', 'c2':'6',
              'a3':'7', 'b3':'8', 'c3':'9']=(
                """
                 ____________________
                |      |      |      |
                | {a1} | {b1} | {c1} | '1' '2' '3'
                |______|______|______|
                |      |      |      |
                | {a2} | {b2} | {c2} | '4' '5' '6'
                |______|______|______|
                |      |      |      |
                | {a3} | {b3} | {c3} | '7' '8' '9'
                |______|______|______|""".strip()
            )
        return board
    
    #Part 3
    # TODO #4 who goes first
    def pickFirst(self):
        return random.randint(0,1)

    def spaceIsFree(pos, board):
        '''Check if space is free on the board'''
        if(board[pos] == ' '):
            return True
        else:
            return False

    def checkTie(board):
        '''Checks board for a Tie'''
        for key in board.keys():
            if board[key] == '':
                return False
            else:
                return True

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


    def minimax(self, board, isMaximizing, computer, player):
        '''criteria for Minimax'''
        self.computer = computer
        self.player = player

        if TicTacToe.checkWin(computer):
            return -100
        elif TicTacToe.checkWin(player):
            return 100
        elif TicTacToe.checkTie():
            return 0
        
        if isMaximizing:
            bestScore = -100
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = computer
                    score = (board, 0, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score 
            return bestScore

        else:
            bestScore = 100
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.player
                    score = self(board, 0, True)
                    if (score < bestScore):
                        bestScore = score
            return bestScore






# Part 7
# Program Logs All Files
# Logs all moves in file(tictactoe.txt)


# PArt 8 Handle input error
print('t') # TODO: check
#raise Exception('Doesnt work')