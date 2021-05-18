import sys
import chess
import time
from boardgrahpics import *
from ai import minimax, ab_pruning


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
    u_move = input("Choose a move from the list: ")
    move = chess.Move.from_uci(u_move)
    return move


def ai_move(board, is_minimax):
    if is_minimax:
        move = minimax(3, chess.Board(board.fen()), True)
    else:
        move = ab_pruning(3, chess.Board(board.fen()), -1000, 1000, True)
    return move[1]


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


def run(is_minimax):
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
            move = ai_move(board, is_minimax)

        else:
            move = human_move(legal_moves)
        # print(move)
        board.push(move)
    game_over_message(board)
    VisualBoard.updateBoard(getPiecePositions(board))
    time.sleep(180)


def main():
    user_inp = input("Enter 0 for minimax or 1 for alpha-beta pruning:\n")
    if user_inp == "1":
        run(False)
    else:
        run(True)


if __name__ == "__main__":
    main()
