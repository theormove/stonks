def solveSudoku(board):
    transponed_board = []

    for i in range(0, 9):
        transponed_board.append([])
        for j in range(0, 9):
            transponed_board[i].append(board[j][i])

    by_squares_board = []

    for i in range(0, 3):
        for t in range(0, 3):
            by_squares_board.append([])

        for j in range(3 * i, 3 * i + 3):
            for k in range(0, 3):
                for p in range(3 * k, 3 * k + 3):
                    by_squares_board[3 * i + k].append(board[j][p])
    print("Sytaert")
    print(by_squares_board)

    available_symbols = [[[] for x in range(9)] for y in range(9)]
    help(board, transponed_board, by_squares_board, available_symbols)


def help(board, transponed_board, by_squares_board, available_symbols):
    not_filled = 0

    for i in range(0, 9):
        for j in range(0, 9):

            if board[i][j] == '.':
                not_filled += 1
                for digit in range(1, 10):
                    if len(available_symbols[i][j]) <= 1:
                        if str(digit) not in board[i] and str(digit) not in transponed_board[j] and str(digit) not in \
                                by_squares_board[int((i - i % 3) + (j - j % 3) / 3)]:
                            available_symbols[i][j].append(str(digit))

                    else:
                        available_symbols[i][j] = []
                        break

                if len(available_symbols[i][j]) == 1:
                    not_filled -= 1
                    board[i][j] = available_symbols[i][j][0]
                    transponed_board[j][i] = available_symbols[i][j][0]
                    by_squares_board[int((i - i % 3) + (j - j % 3) / 3)][(i % 3) * 3 + j % 3] = available_symbols[i][j][
                        0]
                    available_symbols[i][j] = []


    if not_filled > 0:
        print(by_squares_board)
        help(board, transponed_board, by_squares_board, available_symbols)
    else:
        print(board)
        return board

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)