import sys
import chess
import time
from boardgrahpics import *
from ai import minimax


def set_up_endgame(f="6k1/8/4KBB1/8/8/8/8/8"):
    # 8 moves to mate ="6k1/8/4KBB1/8/8/8/8/8"
    # 3 moves to mate = "7k/8/3B1K2/5B2/8/8/8/8"
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
    # print list of legal moves
    for move in legal_moves:
        print(move)

    # get user move as input /
    # TODO: check if legal
    u_move = input("Choose a move from the list")
    move = chess.Move.from_uci(u_move)
    return move

def ai_move(board):
  move = minimax(3, board.copy(), True)[1]

  return move
  

def getFen(board):
    return board.epd().split()[0]


def getPiecePositions(board):
    currFen = getFen(board)
    pieces = ["B", "K", "k"]
    lines = currFen.split("/")
    piecePlaces = {}
    for i in range(len(lines)):
        j = 0
        for char in lines[i]:
            if char not in pieces:
                j += int(char)
            else:
                if char in piecePlaces:
                    piecePlaces[char+"1"] = (i, j)
                else:
                    piecePlaces[char] = (i, j)
                j += 1
    return piecePlaces


def run():
    board = set_up_endgame()
    VisualBoard = BoardGraphics()
    VisualBoard.drawGrid()

    while not board.is_game_over():
        # display board before turn
        board._repr_svg_()
        VisualBoard.updateBoard(getPiecePositions(board))

        print("-----------------------")
        print(board)
        print("-----------------------")

        # move for current player
        legal_moves = list(board.legal_moves)
        move = None
        if board.turn == chess.WHITE:
            # white move
            move = ai_move(board)
        
        else:
            move = human_move(legal_moves)

        board.push(move)
        # print(move)

    game_over_message(board)


def main():
    run()


if __name__ == "__main__":
    main()
