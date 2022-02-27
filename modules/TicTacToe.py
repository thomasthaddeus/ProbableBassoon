from select import select
import board
board = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
import insertLetter

#2 Logging for python file
import logging
logging.basicConfig(filename='ttt_game_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TicTacToe:
    '''Super Class for playing tic tac toe'''
    
    p1 = 'X'
    p2 = 'O'
        
    def __init__(self, player):
        '''defines the player and their choice of X || O'''
        self.player = player
        if player[0]:
            print('X')
        else:
            print('O')
        print("Please choose a player.\n For X's choose player1.{p1}.\n For 'O' choose player2.{p2}")
        
    #prints the board
    def board(self):
        '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
        self.board = board
        board['1':'a1', '2':'b1', '3':'c1',
              '4':'a2', '5':'b2', '6':'c2',
              '7':'a3', '8':'b3', '9':'c3'] = (
                                               'A'    'B'    'C' 
                                            ' _____________________'
                                            '|      |      |      |'
                                            '| {a1} | {b1} | {c1} |'    '1'
                                            '|______|______|______|'
                                            '|      |      |      |'
                                            '| {a2} | {b2} | {c2} |'    '2'
                                            '|______|______|______|'
                                            '|      |      |      |'
                                            '| {a3} | {b3} | {c3} |'    '3'
                                            '|______|______|______|'
                                            )                                                                                      
        return board
        


#check for free spaces 
def spaceIsFree(pos):
    if(board[pos] == ' '):
        return True
    else:
        return False

#check for tie
def checkTie():
    for key in board.keys():
        if board[key] == ' ':
            return False
        
    return True

#check for winner
def isWinner():
    if (board[0] == board[1] and board[0] == board[2] and board[1] != ' '):
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[6] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[0] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[1] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[2] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[0] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

#checks for winner with minimax... mark is x or o
def checkforWinner(self, mark):
    self.mark = mark
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

class Position(TicTacToe):
    #inserts a letter (x,o) on the board 
    def insertLetter(letter, pos):
        '''Rules for placing X's and O's on the board'''
        if spaceIsFree(pos):
            board[pos] = letter
            board()
            if(checkTie()):
                print("Tie Game!")
                exit()

            if isWinner():
                if letter == 'X':
                    print("Computer wins!")
                    exit()
                else:
                    print("Player wins!")
                    exit()
            return    

        else:
            print("That position is taken!")
            pos = int(input("Enter a new position: "))
            insertLetter(letter, pos)
            return

    #player moves
    def playerMove():
        pos = int(input("Enter the position for 'O': "))
        insertLetter(p1, pos)                       # this should be refactored tp cp,ing 
        return

    def compMove():
        bestScore = -1000
        bestMove = 0

        for key in board.keys():
            if(board[key]== ' '):
                board[key] = computer
                score = minimax(board,0,False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
                    bestMove = key

        insertLetter(computer, bestMove)
        return 

#using minimax 
class Minimax(TicTacToe):
    '''Initializes the Class for making 5500 decison tree'''
    def __init__(self, board, player, isMaximizing):
        '''criteria for Minimax class'''
        self.player = player
        if checkforWinner(computer):
            return 100

        elif checkforWinner(player):
            return -100
        
        elif checkTie():
            return 0

        if isMaximizing:
            bestScore = -1000

            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = computer
                    score = (board, 0, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score 

            return bestScore

        else:
            bestScore = 1000
            for key in board.keys():
                if (board[key] == ' '):
                    board[key] = self.player
                    score = self(board, 0, True)
                    if (score < bestScore):
                        bestScore = score
            return bestScore            

# while not isWinner():
#     compTurn = True
#     if compTurn = False:
#         compTurn()
# elif:
#     playerMove

#inserts a letter (x,o) on the board 
def insertLetter(letter, pos):
    if spaceIsFree(pos):
        board[pos] = letter
        printBoard(board)
        if(checkTie()):
            print("Tie Game!")
            exit()

        if isWinner():
            if letter == 'X':
                print("Computer wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return    

    else:
        print("That position is taken!")
        pos = int(input("Enter a new position: "))
        insertLetter(letter, pos)
        return
    
