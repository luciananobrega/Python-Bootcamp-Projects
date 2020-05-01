from board import Board
from player import Player


if __name__ == "__main__":
    board = Board()
    board.show_board()
    
    p1 = Player("X")
    p2 = Player("O")

    pos = p1.play()
    board.update_board(pos, p1.marker)
    board.show_board()
    pos = p2.play()
    board.update_board(pos, p2.marker)
    board.show_board()
