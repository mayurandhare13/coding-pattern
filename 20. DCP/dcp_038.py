def isValid(board: list):
    # 1-D list is represent rows and cols
    # board len is number of rows we filled
    # board index value is column number

    currentQueenRow, currentQueenCol = len(board)-1, board[-1]
    
    for row, col in enumerate(board[:-1]):
        diff = abs(currentQueenCol - col)
        # same column
        if diff == 0:
            return False

        # same diagonal
        if diff == currentQueenRow - row:
            return False

        # we don't have to check for same row
        # as we are placing queen incremently

    return True


def nQueens(n, board=[]):
    if n == len(board):
        return 1

    count = 0

    for col in range(n):
        board.append(col)
        if isValid(board):
            count += nQueens(n, board)

        board.pop()

    return count


if __name__ == '__main__':
    result = [1, 1, 0, 0, 2, 10, 4, 40, 92, 352]

    for i in range(0, 10):
        assert nQueens(i) == result[i]
