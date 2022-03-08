#prints the board
def board(self):
    '''Displays board with index starting in top left and finishing in bottom right [0:8]'''
    self.board = board
    board['1':'a1', '2':'b1', '3':'c1',
          '4':'a2', '5':'b2', '6':'c2',
          '7':'a3', '8':'b3', '9':'c3']=(  'A'    'B'    'C' 
                                      '''_____________________
                                         |      |      |      |
                                         | {a1} | {b1} | {c1} |    '1'
                                         |______|______|______|
                                         |      |      |      |
                                         | {a2} | {b2} | {c2} |    '2'
                                         |______|______|______|
                                         |      |      |      |
                                         | {a3} | {b3} | {c3} |    '3'
                                         |______|______|______|'''
                                        )                                                                                      
    return board