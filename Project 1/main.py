from board import Board
from player import Player

board = Board()
board.show_board()
p1 = Player("X")
p2 = Player("O")

def player1():
    pos = p1.play()
    board.update_board(pos, p1.marker)
    board.show_board()
    if not board.check_winner(p1.marker):
        player2()

def player2():
    pos = p2.play()
    board.update_board(pos, p2.marker)
    board.show_board()
    if not board.check_winner(p2.marker):
        player1()

if __name__ == "__main__":
    player1()