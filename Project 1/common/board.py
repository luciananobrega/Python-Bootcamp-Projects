import os

class Board():
    def __init__(self):
        self.board = list(range(1,10))

    def __str__(self):
        os.system('cls')
        
        return "_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_".format(self.board[6], self.board[7], self.board[8], self.board[3], self.board[4], self.board[5], self.board[0], self.board[1], self.board[2])
    
    def update_board(self, position, marker):
        self.board[position - 1] = marker

    def check_winner(self, player):
        if self.board[0] == self.board[1] == self.board[2] or self.board[3] == self.board[4] == self.board[5] or \
            self.board[6] == self.board[7] == self.board[8] or self.board[0] == self.board[3] == self.board[6] or \
            self.board[1] == self.board[4] == self.board[7] or self.board[2] == self.board[5] == self.board[8] or \
            self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]:
            print("Player {} wins!".format(player))
            return True
        else:
            return False

    def check_full(self):
        return all(isinstance(x, str) for x in self.board)

    def valid_position(self, pos):
        if self.board[pos-1] != "X" and self.board[pos-1] != "O":
            return True
        else:
            print("Position already chosen. Try again.")
            return False
