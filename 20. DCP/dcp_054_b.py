from collections import defaultdict


m = 3
n = m * m

# calc box index
boxIndex = lambda row, col: (row // m) * m + col // m

# use dict to quickly check if num is present in Row, Col & Box
# reducing TC from O(n) to O(1)
rows = [defaultdict(bool) for i in range(n)]
cols = [defaultdict(bool) for i in range(n)]
boxes = [defaultdict(bool) for i in range(n)]


def isValid(d, r, c) -> bool:
    return not (d in rows[r] or d in cols[c] or \
                d in boxes[boxIndex(r, c)])


def placeNumber(d, r, c):
    rows[r][d] = True
    cols[c][d] = True
    boxes[boxIndex(r, c)][d] = True
    board[r][c] = str(d)


def removeNumber(d, r, c):
    del rows[r][d]
    del cols[c][d]
    del boxes[boxIndex(r, c)][d]
    board[r][c] = '.'


def sudoku(r = 0, c = 0):
    if r == n - 1 and c == n:
        return True
    
    if c == n:
        c = 0
        r += 1
    
    if board[r][c] != '.':
        return sudoku(r, c + 1)
    
    for d in range(1, n + 1):
        if isValid(d, r, c):
            placeNumber(d, r, c)
            if sudoku(r, c + 1):
                return True
        
            removeNumber(d, r, c)

    return False


def init():
    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                d = int(board[i][j])
                placeNumber(d, i, j)


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

    init()

    # O(9!^9) <-- because of caching. we find invalid num in O(1)
    if sudoku():
        for row in board:
            for c in row:
                print(c, end=' ')
            print()
    else:
        print('solution does not exists.')
