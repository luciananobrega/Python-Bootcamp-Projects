class Player:
    pass
    """
    def player1(self):
        if not Board.check_result(self, board):
            try:
                p1 = int(input("Player 1, choose a position: "))
            except:
                print("Invalid position. Try again.")
                self.count -= 1
                p1 = 0
                self.player1()
            if Board.check_position(self, p1 - 1):
                self.board[p1 - 1] = "X"
                Board.show_board(self)
                self.player2()
            else:
                self.player1()

    def __player2(self):
        if not Board.check_result(self, board):
            try:
                p2 = int(input("Player 2, choose a position: "))
            except:
                print("Invalid position. Try again.")
                self.count -= 1
                p2 = 0
                self.player2()
            if Board.check_position(self, p2 - 1):
                self.board[p2-1] = "O"
                Board.show_board(self)
                self.player1()
            else:
                self.player2()"""