def draw():
    # initialize an empty board
    board = '''
     {} | {} | {} 
    ____|____|____
        |    |    
     {} | {} | {} 
    ____|____|____
        |    |    
     {} | {} | {} ''' 

    # there are 5 rows in a standard tic-tac-toe board
    for i in range(5):
        # switch between printing vertical and horizontal bars
        if i%2 == 0:
            board += "___|" * 2
        # don't forget to start a new line after each row using "\n"
        board += "\n"

    print(board)

draw()