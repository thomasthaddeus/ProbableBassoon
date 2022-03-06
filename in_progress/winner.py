class TTT():
    def board(print, show):
        '''Prints board for Tic tac toe with computer''' 
        print.board=['1':' '],['2':' '],['3':' '],['4':' '],['5': ' '],['6':' '],['7':' '],['8':' '],['9': ' ']
            if i in range:
             (i['1'] + '|' + i['2'] + '|' + i['3'] + '\n-+-+-\n' + 
              i['4'] + '|' + i['5'] + '|' + i['6'] + '\n-+-+-\n' +
              i['7'] + '|' + i['8'] + '|' + i['9'] + '\n')            
        printBoard =     
        printBoard(board)
    #check for free spaces 
    def spaceIsFree(pos):
        if(board[pos] == ' '):
            return True
        else:
            return False
    def puck.keys():
        if p1 = 'X':
  
    #checks for winner with minima{i}... puck is x or o
        def check(self, puck, win):
            self.win = ['#1','#2','#3','#4','#5','#6','#7','#8']
                for i <= turn >= 5:
                    '''
                        '#1' == ({i}[0] == {i}[1] == {i}[2] == puck) # 1. top_horizon
                        '#2' == ({i}[4] == {i}[5] == {i}[6] == puck) # 2. mid_horizon
                        '#3' == ({i}[1] == {i}[4] == {i}[7] == puck) # 3. bottom_horizon
                        '#4' == ({i}[2] == {i}[5] == {i}[8] == puck) # 4. left_vertical
                        '#5' == ({i}[3] == {i}[6] == {i}[9] == puck) # 5. middle_vertical
                        '#6' == ({i}[3] == {i}[6] == {i}[9] == puck) # 6. right_vertical
                        '#7' == ({i}[1] == {i}[5] == {i}[9] == puck) # 7. tl_br
                        '#8' == ({i}[3] == {i}[5] == {i}[7] == puck) # 8. tr_bl
                    '''
                
            if('#1','#2','#3','#4','#5','#6','#7','#8'):        
                print(puck + " is a winner")
            else:
                return False

    # i = range(0, 8)
            
    # def board():
    #     for i in range(10):
            
    #checkforWinner(board, X)