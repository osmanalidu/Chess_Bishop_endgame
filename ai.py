import chess

def heuristic(board):
  #Stalemate = 0, ai win = 1 (black can at best stalemate)
  #Restrict black movement without stalemate
  #Checking is good 

  return 1 if board.is_checkmate else -len(board.legal_moves)



def minimax(depth, board, is_max):
  if depth == 0 or board.is_game_over: 
    return heuristic(board), 0000

  if is_max:
    score = -1000
    legal_moves = list(board.legal_moves)
    best = legal_moves[0]
    
    for move in legal_moves:
      #pass in board after move
      min_val = minimax(depth-1, board.push(move), False)[0]
      score = max(score, min_val)
      best = move
    
    return score, best
  else:
    score = 1000
    legal_moves = list(board.legal_moves)
    best = legal_moves[0]
    
    for move in legal_moves:
      #pass in board after move
      max_val = minimax(depth-1, board.push(move), True)[0]
      score = min(score, max_val)
      best = move
    
    return score, best
