# Random integer in place of the the minimax algorithm unless 
# minimax works



board = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
import insertLetter

#2 Logging for python file
import logging
logging.basicConfig(filename='ttt_game_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class TicTacToe:
    '''Super Class for playing tic tac toe'''
    
    p1 = 'X'
    p2 = 'O'
        
    def __init__(self, player, computer):
        '''defines the player and their choice of X || O'''
        
        self.player = player
        self.computer = computer
        print("Please choose a player.\n For X's choose player1.{p1}.\n For 'O' choose player2.{p2}")
        if player:              # Call the player
            print
            print('X')
        else:
            print('O')
        
        
    #prints the board
    def board(self):
        '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
        self.board = board
        board['a1':'1', 'b1':'2', 'c1':'3',
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

def spaceIsFree(pos):
    '''Check if space is free on the board'''
    if(board[pos] == ' '):
        return True
    else:
        return False

def checkTie():
    '''Checks board for a Tie'''
    for key in board.keys():
        if board[key] == ' ':
            return False
        else:
            return True

#using minimax 
class Minimax(TicTacToe):
    '''Initializes the Class for making decison tree'''
    
    def __init__(self, board, computer, player, isMaximizing):
        '''criteria for Minimax class'''
        
        self.computer = computer
        self.player = player
        TicTacToe.board = board
        
        if TicTacToe.checkWin(computer):
            return -100

        elif checkWin(player):
            return 100
        
        elif checkTie():
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

class Position(TicTacToe):
    ''' #inserts a letter (x,o) on the board''' 
    def insertLetter(mark, pos):
        '''Rules for placing X's and O's on the board'''
        if spaceIsFree(pos):
            board[pos] = mark
            print(board())
            if(checkTie()):
                print("Tie Game!")
                exit()

            if checkforWinner():
                if mark == 'X':
                    print("Computer wins!")
                    exit()
                else:
                    return("Player wins!")  

        else:
            print("That position is taken!")
            pos = int(input("Enter a new position: "))
            return 

    #player moves
    def playerMove(player):
        pos = int(input("Enter the position for 'O': "))
        insertLetter(player, pos)                       # this should be refactored tp cp,ing 
        return

    def compMove(computer):
        bestScore = -100
        bestMove = 0

        for key in board.keys():
            if(board[key]== ' '):
                board[key] = computer
                score = Minimax(board,0,False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
                    bestMove = key

        insertLetter(computer, bestMove)
        return 
