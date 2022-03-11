###################################
#          TIC TAC TOE            #
#  by Stephanie Ort, Thad Thomas  #
#            IS 201               #
#    Fundamentals of Computing    #
###################################

import random
import logging
logging.basicConfig(filename='ttt_game_log.txt', 
                    filemode='w', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# class TicTacToe:
#Class for playing TicTacToe''' '''

welcome = ("Welcome to Tic Tac Toe\n")
directions = ("""
                First: Choose your piece: X or O.
                \nThe computer randomly decides who goes first.
                \nThen pick a spot on the board.
                \nUse the numbers 1-9 to pick a spot on the board.""")

    
def getuserPiece(piece):
    """Defines which piece the user is and whether they go first or second"""
    piece = ""
    while piece != 'X' and piece != 'O':
        piece = input("To Play Please Select Either (X)'s or (O)'s: ").capitalize
    p1 = piece
    if p1 == 'X':
        p2 = 'O'
    else: 
        p1 = 'X'

    if random.randint == 0:
        print("Player goes first")
    else:
        print("Computer goes first")
    
    print(p1,"Player\n", p2, "Computer")
    return p1, p2

def drawBoard(self,board):
    '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
    self.board=board("____________________ \n|      |      |      |\n| {a1} | {b1} | {c1} | 1 2 3\n|______|______|______|\n|      |      |      |\n| {a2} | {b2} | {c2} | 4 5 6\n|______|______|______|\n|      |      |      |\n| {a3} | {b3} | {c3} | 7 8 9\n|______|______|______|".format(a1='1',b1='2',c1='3',a2='4',b2='5',c2='6',a3='7',b3='8',c3='9'))
    return board

def copy_board(board):
    """Displays copy of the board"""
    copy = []
    for i in board:
        copy.append(i)
    return copy

def makeMove(board, move, piece):
    """Displays move"""
    if spaceIsFree(move):
        board[move] = piece
        try:
            x = input('Give me a number between 1 and 9: ')
            if x == 'q':
                exit
            x=int(x)
        except ValueError:
            print('Invalid number')
        else:
            print    
        if(checkTie()):
            print("Tie Game!")

        elif checkWin():
            if piece == 'X':
                print("Computer wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return    

    else:
        print("That position is taken!")
        input("Enter a new position: ")
        
        return


    
def spaceIsFree(board, move):
    '''Check if space is free on the board'''
    if(board[move] == ' '):
        return True

def checkTie(board):
    '''Checks board for a Tie'''
    logging.info("Checking for a tie")
    for key in board.keys():
        if board[key] == '':
            return False
        else:
            return "Game is a Tie"

def checkWin():
    '''Checks for winner using the board'''
    i, mark = 
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

logging.info('Start of Program')
def main():
    """Loop for running Game"""
    print(welcome, directions)
    while True:
        drawBoard()
        getuserPiece()
        turn = 'X'
        for i in range(9):
            drawBoard()
            print('It is' + turn + '. Move on which space?')
            move = input()
            drawBoard[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        drawBoard(board)
            
if __name__ == '__main__':
    main()

logging.info('End of Program')