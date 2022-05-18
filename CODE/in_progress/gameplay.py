
print("""
###################################
#          TIC TAC TOE            #
#  by Stephanie Ort, Thad Thomas  #
#            IS 201               #
#    Fundamentals of Computing    #
###################################
""")

import random
import logging
logging.basicConfig(filename='ttt_game_log.txt', 
                    filemode='w', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of Program')
def main():
    """main _summary_"""
    print()
    
    
if __name__ == '__main__':
    main()
logging.info('End of Program')

n = 3

mat = [['.'] * n  for i in range(n)]



win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]

# Main function: alternately prompt the two human
# players – 'X' and 'O' – by calling get_move function.
#

def main():
    num_moves = 0
    print_mat()
    print('Moves are r, c or "0" to exit.')
    exit_flag = False

    while not exit_flag:
        num_moves += 1
        if num_moves > 9:
            print('No more space left.')
            break
        player_ch = 'X' if num_moves % 2 > 0 else 'O'
        exit_flag, r, c = get_move(player_ch)
        if (not exit_flag) and   test_win(r, c):
            print('\n', player_ch, 'WINS THE GAME!')
            break

# Get Move function.
# Prompt and re-prompt human player ('X' or 'O')
# until a valid move of form 'row, col' has been
# entered at an available square. Then enter move
# into the grid and re-print the grid display.
def get_move(player_ch):
    while True:
        prompt = 'Enter move for ' + player_ch + ': '
        s = input(prompt)
        a_list = s.split(',')
        if len(a_list) >= 1 and int(a_list[0]) == 0:
            print('Bye now.')
            return True, 0, 0
        elif len(a_list) < 2:
            print('Use row, col. Re-enter.')
        else:
            # First, convert to 0-based indexes.
            r = int(a_list[0]) - 1
            c = int(a_list[1]) - 1
            if r < 0 or r >= n or c < 0 or c >=   n:
                 print('Out of range. Re-enter.')
            elif mat[r][c] != '.':
                 print('Occupied square. Re-enter.')
            else:
                 mat[r][c] = player_ch
                 print_mat()
                 break
    return False, r, c

                             

def print_mat():
    s = '  1 2 3\n'
    for i in range(n):
        s += str(i + 1) + ' '
        for j in range(n):
            s += str(mat[i][j]) + ' '
        s += '\n'
    print(s)

# Test Win function.
# win_list = List of all winning   combinations.
# ttt_list = an individual list, such as   [1, 2, 3],
#   that holds one winning Tic-Tac-Toe   combination.
# my_win_list = list of all ttt_list   instances
#   that contain the current cell.
# Function tests all the combos in   my_win_list.
# A combo returns True if it has 3 Xs or   3 Os.
#
def test_win(r, c):
    cell_n = r * 3 + c + 1   # Get cell   num. 1 to 9.
    my_win_list = [ttt_list for ttt_list   in win_list
                   if cell_n in   ttt_list]
    for ttt_list in my_win_list:
        num_x, num_o, num_blanks =   test_way(ttt_list)
        if num_x == 3 or num_o == 3:
            return True
    return False

def test_way(cell_list):
    letters_list = []
    # Create list of the form ['X', '.',   'O']
    for cell_n in cell_list:
        r = (cell_n - 1) // 3
        c = (cell_n - 1) % 3
        letters_list.append(mat[r][c])
    num_x = letters_list.count('X')  #   How many X's?
    num_o = letters_list.count('O')  #   How many O's?
    num_blanks = letters_list.count('.')
    return num_x, num_o, num_blanks

main()

x=abs(int(float(-4.5+3.2)))
print(x-1j)