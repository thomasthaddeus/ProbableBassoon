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