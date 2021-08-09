# refer dcp_062.py

EMPTY = 0
WALL = 1

def numWays(matrix: list[list]):
    m, n = len(matrix), len(matrix[0])
    numWaysMatrix = [[0 for _ in range(n)] for _ in range(m)]

    # fill topmost row
    for j in range(n):
        if matrix[0][j] == WALL:
            break
        numWaysMatrix[0][j] = 1
    
    # fill leftmost column
    for i in range(m):
        if matrix[i][0] == WALL:
            break
        numWaysMatrix[i][0] = 1
    

    for i in range(1, m):
        for j in range(1, n):
            fromTop = numWaysMatrix[i - 1][j] if matrix[i - 1][j] == EMPTY else 0
            fromLeft = numWaysMatrix[i][j - 1] if matrix[i][j - 1] == EMPTY else 0

            if matrix[i][j] == EMPTY:
                numWaysMatrix[i][j] = fromTop + fromLeft

    return numWaysMatrix[m - 1][n - 1]


if __name__ == '__main__':
    mat = [[0, 0, 1],
            [0, 0, 1],
            [1, 0, 0]]

    # O(n * m) time and space
    assert numWays(mat) == 2

