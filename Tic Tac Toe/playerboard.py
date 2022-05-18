def drawBoard(board):
    '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
    board("____________________ \n|      |      |      |\n| {a1} | {b1} | {c1} | 1 2 3\n|______|______|______|\n|      |      |      |\n| {a2} | {b2} | {c2} | 4 5 6\n|______|______|______|\n|      |      |      |\n| {a3} | {b3} | {c3} | 7 8 9\n|______|______|______|".format(a1='1',b1='2',c1='3',a2='4',b2='5',c2='6',a3='7',b3='8',c3='9'))
    
    return board
drawBoard = f"{},{},{},{},{},{},{},{},{}".format()
print(drawBoard(board))