from board import Board
from player import Player

board = Board()
print(board)
p1 = Player("X")
p2 = Player("O")

def player1():
    pos = p1.play()
    if pos and board.valid_position(pos):
        board.update_board(pos, p1.marker)
        print(board)
        if not board.check_winner(p1.marker):
            if board.check_full():
                print("Drawn")
            else:
                player2()
    else:
        player1()

def player2():
    pos = p2.play()
    if pos and board.valid_position(pos):
        board.update_board(pos, p2.marker)
        print(board)
        if not board.check_winner(p2.marker):
            if board.check_full():
                print("Drawn")
            else:
                player1()
    else:
        player2()

if __name__ == "__main__":
    player1()