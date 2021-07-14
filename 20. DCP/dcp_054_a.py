M = 9

def printGrid(grid):
    for row in grid:
        for c in row:
            print(c, end=' ')
        print()
    

def isValid(grid: list[list], row, col, num):
    for x in range(M):
        if grid[row][x] == str(num):
            return False

        if grid[x][col] == str(num):
            return False

    # check box
    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(M // 3):
        for j in range(M // 3):
            if grid[i + startRow][j + startCol] == str(num):
                return False
    
    return True



def sudoku(grid: list[list], row, col):
    if row == M - 1 and col == M:
        return True
    
    if col == M:
        row += 1
        col = 0
    
    if grid[row][col] != '.':
        return sudoku(grid, row, col + 1)

    for num in range(1, M + 1):
        if isValid(grid, row, col, num):
            grid[row][col] = str(num)
            if sudoku(grid, row, col + 1):
                return True

            grid[row][col] = '.'
    
    return False


# --------------------------------------------------------

def validSudoku(board: list[list]) -> bool:
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(i, c), (c, j), (i/3, j/3, c)]
    
    return len(seen) == len(set(seen))


if __name__ == '__main__':
    board = [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]

    assert validSudoku(board) == True

    # O(9^81)
    if sudoku(board, 0, 0):
        printGrid(board)
    else:
        print('solution does not exists.')
