import chess

def set_up_endgame(f = "7k/8/3B1K2/5B2/8/8/8/8"):
  #8 moves to mate ="6k1/8/4KBB1/8/8/8/8/8"
  #3 moves to mate = "7k/8/3B1K2/5B2/8/8/8/8"
  # - Kg6, kg8, Be6+, kh8, Be5#
  return chess.Board(f)

def game_over_message(board):
  print("\n\nFinal Position:\n", board)
  if board.is_checkmate():
    if board.turn == chess.WHITE:
      print("Black Wins")
    else:
      print("White Wins")
  else:
    print("Draw")

def human_move(legal_moves):
  #print list of legal moves
  for move in legal_moves:
    print(move)

  #get user move as input / 
  #TODO: check if legal
  u_move = input("Choose a move from the list")
  move = chess.Move.from_uci(u_move)
  return move

def run():
  board = set_up_endgame()
  
  while not board.is_game_over():
    #display board before turn
    board._repr_svg_()

    print("-----------------------")
    print(board)
    print("-----------------------")

    #move for current player
    legal_moves = list(board.legal_moves)
    move = None
    if board.turn == chess.WHITE:
      #white move
      move = legal_moves[0]
    else:
      move = human_move(legal_moves)
    
    board.push(move)
    # print(move)

  game_over_message(board)
  

run()