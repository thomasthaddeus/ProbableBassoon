#inserts a letter (x,o) on the board 
def insertLetter(self, letter, pos):
    if spaceIsFree(pos):
        board[pos] = letter
        printBoard(board)
        if(checkTie()):
            print("Tie Game!")

        elif isWinner():
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
    
    
    
        '''Who goes first'''
    logging.info("randomly assigns player one")
    ''' i = X != O
    for i in range(0,1):
        if random.randint(0,1)==0:
            if i is 'O':
                yield 'X'
            else: 'O' '''