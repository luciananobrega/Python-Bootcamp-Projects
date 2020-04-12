def show_board(board):
    print("_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_".
        format(board[6], board[7], board[8], board[3], board[4], board[5], board[0], board[1], board[2]))

def player1(board):
    if not winner(board):
        show_board(board)
        p1 = int(input("Player 1, choose a position: "))
        board[p1-1] = "X"
        player2(board)

def player2(board):
    if not winner(board):
        show_board(board)
        p2 = int(input("Player 2, choose a position: "))
        board[p2-1] = "O"
        player1(board)

def winner(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        if board[0] == "X":
            print("Player 1 wins!")
            return 1
        elif board[0] == "O":
            print("Player 2 wins!")
            return 1
        else:
            return 0
    elif board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        if board[0] == "X":
            print("Player 1 wins!")
        elif board[0] == "O":
            print("Player 2 wins!")
        else:
            return 0
    elif board[0] == board[4] == board[8] or board[2] == board[6] == board[8]:
        if board[0] == "X":
            print("Player 1 wins!")
            return 1
        elif board[0] == "O":
            print("Player 2 wins!")
            return 1
        else:
            return 0
    else:
        return 0

if __name__ == "__main__":
    board = list(range(1,10))
    player1(board)