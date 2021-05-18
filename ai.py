import chess


def heuristic(board):
    # Stalemate = 0, ai win = 1 (black can at best stalemate)
    # Restrict black movement without stalemate
    #Checking is good
    n_moves = len(list(board.legal_moves))
    if board.is_checkmate():
        return 1
    return -10000 if n_moves == 0 else -len(list(board.legal_moves))



def minimax(depth, board, is_max):
    if depth == 0 or board.is_game_over():
        return heuristic(board), "0000"

    if is_max:
        score = -1000
        legal_moves = list(board.legal_moves)
        best = legal_moves[0]

        for move in legal_moves:
            # print("max: " + str(move))
            # pass in board after move
            n_board = chess.Board(board.fen())
            n_board.push(move)
            min_val = minimax(depth-1, n_board, False)[0]
            if min_val > score:
                score = min_val
                best = move
        return score, best

    else:
        score = 1000
        legal_moves = list(board.legal_moves)
        best = legal_moves[0]

        for move in legal_moves:
            # print("min: " + str(move))
            # pass in board after move
            m_board = chess.Board(board.fen())
            m_board.push(move)
            max_val = minimax(depth-1, m_board, True)[0]
            if max_val < score:
                score = max_val
                best = move
        return score, best




def ab_pruning(depth, board, alpha, beta, is_max):
    if depth == 0 or board.is_game_over():
        return heuristic(board), "0000"

    if is_max:
        score = -1000
        legal_moves = list(board.legal_moves)
        best = legal_moves[0]

        for move in legal_moves:
            # print("max: " + str(move))
            # pass in board after move
            n_board = chess.Board(board.fen())
            n_board.push(move)
            min_val = ab_pruning(depth-1, n_board, alpha, beta, False)[0]
            if min_val > score:
                score = min_val
                best = move
            alpha = max(alpha, min_val)
            if beta <= alpha:
                break
        return score, best

    else:
        score = 1000
        legal_moves = list(board.legal_moves)
        best = legal_moves[0]

        for move in legal_moves:
            # print("min: " + str(move))
            # pass in board after move
            m_board = chess.Board(board.fen())
            m_board.push(move)
            max_val = ab_pruning(depth-1, m_board, alpha, beta, True)[0]
            if max_val < score:
                score = max_val
                best = move
            beta = min(beta, max_val)
            if beta <= alpha:
                break
        return score, best
