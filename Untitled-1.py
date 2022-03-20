class MiniMax:
    '''algorithm for minimax'''

    def make_best_move(board):
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