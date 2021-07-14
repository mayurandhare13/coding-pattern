def gameOfLife(board: list[list]) -> None:
    neighbors = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        for col in range(cols):
            aliveCells = 0
            for r, c in neighbors:
                R = r + row
                C = c + col

                if (R >= 0 and R < rows) and (C >= 0 and C < cols) and abs(board[R][C]) == 1:
                    aliveCells += 1
            
            # set prev alive as -1
            if board[row][col] ==  1 and (aliveCells < 2 or aliveCells > 3):
                board[row][col] = -1

            if board[row][col] == 0 and aliveCells == 3:
                board[row][col] = 2


    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 2:
                board[row][col] = 1
            
            if board[row][col] == -1:
                board[row][col] = 0


if __name__ == '__main__':
    board = [[1, 1], [1, 0]]
    gameOfLife(board) # [[1, 1], [1, 1]]

    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    gameOfLife(board) # [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
