def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "

        print(row_str)
        if i != len(board) - 1:
            print("-" * 11)


# def get_move(turn, board):
#     while True:
        

#         if row < 1 or row > len(board):
#             print("Invalid row, try again")
#         elif col < 1 or col > len(board[row - 1]):
#             print("Invalid col, try again")
#         elif board[row - 1][col - 1] == "X" or board[]:
#             print("Already taken, try again")
#         else:
#             break
#     board[row - 1][col - 1] = turn

def get_move(choice,board):
    turn = "X"
    for i in range(len(board)):
        for j in range(len(board[i])):
            if choice == board[i][j]:
                board[i][j] = turn;
                if board[i][j] == turn:
                    print("Already taken, try another spot")
                    continue
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"  
                
                
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

print_board(board)
choice = input("Enter your choice")
get_move(choice,board)
print_board(board)