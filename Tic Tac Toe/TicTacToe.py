import spaceisfree
#tic tac toe with computer 
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

#prints the board
'''def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print("\n")'''
# printBoard(board)

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

player = 'O'
computer = 'X'

#player moves
def playerMove():
    pos = int(input("Enter the position for 'O': "))
    insertLetter(player, pos)
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
def minimax(board, depth, isMaximizing):

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
                score = minimax(board, 0, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score 

        return bestScore

    else:
        bestScore = 1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, 0, True)
                if (score < bestScore):
                    bestScore = score
        return bestScore            

while not isWinner():
    compMove()
    playerMove()
