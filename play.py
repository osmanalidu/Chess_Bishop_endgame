import chess

def run():
  board = chess.Board()
  
  
  while not board.is_game_over():
    #display board before turn
    board._repr_svg_()
    print(board)

    #move for current player
    legal_moves = list(board.legal_moves)
    if board.turn == chess.WHITE:
      #white move
      board.push(legal_moves[0])
    else:
      board.push(legal_moves[0])