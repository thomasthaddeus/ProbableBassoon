
# Tic-Tac-Toe

import random

def main():
    '''Main program'''
    print('Welcome to Tic-Tac-Toe!')
    while True:
        # Reset the board.
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                # Player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break

                    else:
                        turn = 'computer'
            else:
                # Computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break

def drawBoard(board):
    """This function prints out the board that it was passed."""
    print(board[0] + '|' + board[1] + '|' + board[2] + 'tt1 2 3')
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5] + 'tt4 5 6')
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8] + 'tt7 8 9')


def inputPlayerLetter():
    """ Lets the player type which letter they want to be.
        Returns a list with the player's letter as the first item and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):

        print('Do you want to be X or O?')
        letter = input().upper()

# The first element in the list is the player's letter; the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    """ Randomly choose which player goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    """given a board and player's letter,this function returns True if that player has won
       We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
    """
    return (
            (bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le)
    )

def getBoardCopy(board):
    """Make a copy of the board list and return it."""
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    """ Return True if the passed move is free on the passed board."""
    return board[move] == ' '

def isBoardFull(board):
    """ Return True if every space on the board has been taken. Otherwise, return False."""
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True

def chooseRandomMoveFromList(board, movesList):
    """Returns a valid move from the passed list on the passed board.
       Returns None if there is no valid move.
    """
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    """Given a board and the computer's letter, determine where to move and return that move."""
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
    # Here is the algorithm for our Tic-Tac-Toe :
    # First, check if we can win in the next move.
    for i in range(0, 9):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    # Check if the player could win on their next move and block them.
    for i in range(0, 9):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    # Try to take one of the corners, if they are free.
        move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
        if move != None:
            return move
    # Try to take the center, if it is free.
        if isSpaceFree(board, 4):
            return 4
    # Move on one of the sides.
        return chooseRandomMoveFromList(board, [1, 3, 5, 7])

def isBoardFull(board):
    """ Return True if every space on the board has been taken. Otherwise, return False."""
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True

def getPlayerMove(board):
    """ Let the player enter their move."""
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
        return int(move) - 1
    
if __name__ == '__main__':
    main()
    