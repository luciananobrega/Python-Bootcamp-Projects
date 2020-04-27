class TicTacToe():
    def __init__(self):
        self.board = list(range(1,10))
        self.show_board()
        self.count = 0
        self.player1()

    def show_board(self):
        print("_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_".
            format(self.board[6], self.board[7], self.board[8], self.board[3], self.board[4], self.board[5], self.board[0], self.board[1], self.board[2]))

    def player1(self):
        if not self.winner():
            try:
                p1 = int(input("Player 1, choose a position: "))
            except:
                print("Invalid position. Try again.")
                self.player1()
            if self.check_position(p1 - 1):
                self.board[p1-1] = "X"
                self.show_board()
                self.player2()
            else:
                self.player1()

    def player2(self):
        if not self.winner():
            try:
                p2 = int(input("Player 2, choose a position: "))
            except:
                print("Invalid position. Try again.")
                self.player2()
                
            if self.check_position(p2 - 1):
                self.board[p2-1] = "O"
                self.show_board()
                self.player1()
            else:
                self.player2()

    def check_position(self, pos):
        if self.board[pos] != "X" and self.board[pos] != "O":  
            return 1
        else:
            print("Position already chosen. Play again")
            return 0

    def winner(self):
        if self.board[0] == self.board[1] == self.board[2] or self.board[0] == self.board[3] == self.board[6] or self.board[0] == self.board[4] == self.board[8]:
            if self.board[0] == "X":
                print("Player 1 wins!")
                return 1
            elif self.board[0] == "O":
                print("Player 2 wins!")
                return 1
            else:
                self.count += 1
                return 0
        elif self.board[3] == self.board[4] == self.board[5] or self.board[1] == self.board[4] == self.board[7] or self.board[2] == self.board[4] == self.board[6]:
            if self.board[4] == "X":
                print("Player 1 wins!")
                return 1
            elif self.board[4] == "O":
                print("Player 2 wins!")
                return 1
            else:
                self.count += 1
                return 0
        elif self.board[6] == self.board[7] == self.board[8] or self.board[2] == self.board[5] == self.board[8]:
            if self.board[8] == "X":
                print("Player 1 wins!")
                return 1
            elif self.board[8] == "O":
                print("Player 2 wins!")
                return 1
            else:
                self.count += 1
                return 0
        else:
            if self.count == 9:
                print("Drawn")
                return 1
            else:
                self.count += 1
                return 0

if __name__ == "__main__":
    game = TicTacToe()