import os

class Board():
    def __init__(self):
        self.board = list(range(1,10))

    def show_board(self):
        def clear():
            os.system( 'cls' )
        clear()
        
        print("_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_".
            format(self.board[6], self.board[7], self.board[8], self.board[3], self.board[4], self.board[5], self.board[0], self.board[1], self.board[2]))
    
    def update_board(self):
        pass

    def check_winner(self, player):
        if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or \
            board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or \
            board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or \
            board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
            print("Player {} wins!".format(player))
            return True
        else:
            return False

    def check_full(self):
        pass


class Position():
    def check_position(self, pos):
        if self.board[pos] != "X" and self.board[pos] != "O":
            return 1
        else:
            print("Position already chosen. Try again")
            self.count -= 1
            return 0
