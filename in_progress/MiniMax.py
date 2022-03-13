import numpy as np

class MiniMax:
    '''algorithm for minimax'''    
    
    def make_best_move(board):
        best_score = -np.inf
        best_move = None
        for move in ticTacBoard.get_possible_moves():
            ticTacBoard.make_move(move)
            score = minimax(False, computer, board)
            ticTacBoard.undo()
            if (score > bestScore):
                best_score = score
                best_move = move
        ticTacBoard.make_move(best_move)

    def minimax(isMaxTurn, maximizerMark, board):
        state = board.get_board()
        if (state is State.DRAW):
            return 0
        elif (state is State.OVER):
            return 1 if board.get_winner() is maximizerMark else -1

        score = []
        for move in board.get_possible_moves():
            board.make_move(move)
            score.append(minimax(not isMaxTurn, maximizerMark, board))
            board.undo()

        return max(score) if isMaxTurn else min(score)


class MiniMaxMax:
    ''''''

    def score(game, depth):
        ''''''
        if game.win(player):
            return 10 - depth
        elif game.win('computer'):
            return depth - 10
        else:
            return 0


    def minimax(game, depth)
        return score(game) if game.over?
        depth += 1
        scores = [] # an array of scores
        moves = []  # an array of moves

        # Populate the scores array, recursing as needed
        game.get_available_moves.each do |move|
            possible_game = game.get_new_state(move)
            scores.push minimax(possible_game, depth)
            moves.push move
        end

        # Do the min or the max calculation
        if game.active_turn == @player
            # This is the max calculation
            max_score_index = scores.each_with_index.max[1]
            @choice = moves[max_score_index]
            return scores[max_score_index]
        else
            # This is the min calculation
            min_score_index = scores.each_with_index.min[1]
            @choice = moves[min_score_index]
            return scores[min_score_index]