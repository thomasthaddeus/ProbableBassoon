'''
Minimax doc string
'''
import numpy as np

class MiniMax:
    '''algorithm for minimax'''

    def make_best_move(self,board,p_2):
        '''returns the best move for minimax'''
        best_score = -np.inf
        best_move = None
        for move in empty_space.get_possible_moves():
            ticTacBoard.make_move(move)
            score = minimax(False, computer, board)
            ticTacBoard.undo()
            if (score > best_score):
                best_score = score
                best_move = move
        ticTacBoard.make_move(best_move)

    def minimax(computer_turn, computer_piece, board):
        '''Define Minimax'''
        state = board.get_board()
        if (state is State.DRAW):
            return 0
        elif (state is State.OVER):
            return 1 if board.get_winner() is computer_piece else -1

        score = []
        for move in board.get_possible_moves():
            board.make_move(move)
            score.append(minimax(not computer_turn, computer_piece, board))
            board.undo()

        return max(score) if computer_turn else min(score)




# class MiniMaxMax:
#     ''''''

#     def score(game, depth):
#         ''''''
#         if game.win(player):
#             return 10 - depth
#         elif game.win('computer'):
#             return depth - 10
#         else:
#             return 0


#     def minimax(game, depth)
#         return score(game) if game.over?
#         depth += 1
#         scores = [] # an array of scores
#         moves = []  # an array of moves

#         # Populate the scores array, recursing as needed
#         game.get_available_moves.each do |move|
#             possible_game = game.get_new_state(move)
#             scores.push minimax(possible_game, depth)
#             moves.push move
#         end

#         # Do the min or the max calculation
#         if game.active_turn == @player
#             # This is the max calculation
#             max_score_index = scores.each_with_index.max[1]
#             @choice = moves[max_score_index]
#             return scores[max_score_index]
#         else
#             # This is the min calculation
#             min_score_index = scores.each_with_index.min[1]
#             @choice = moves[min_score_index]
#             return scores[min_score_index]


# old minimax
# def minimax(board): # still not implemented
#     '''criteria for Minimax'''
#     if check_win == False:
#         return -100
#     elif check_win == True:
#         return 100
#     elif check_tie():
#         return 0

    # if max:
    #     bestScore = -100
    #     for key in BOARD_KEYS:
    #         if (board[key] == ''):
    #             board[key] = False
    #             score = (board, 0, False)
    #             return False
    #         elif (score > bestScore):
    #             bestScore = score
    #     return bestScore

    # else:
    #     bestScore = 100
    #     for key in BOARD_KEYS:
    #         if (board[key] == ''):
    #             board[key] = True
    #             score = (board, 0, True)
    #             if (score < bestScore):
    #                 bestScore = score
    #     return bestScore
