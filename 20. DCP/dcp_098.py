def search(board: list[list], r, c, visited: set, index, word):
    def isValid(r, c):
        return r >= 0 and r < len(board) and \
            c >= 0 and c < len(board[0])
    
    if not isValid(r, c):
        return False
    
    if (r, c) in visited:
        return False
    
    if board[r][c] != word[index]:
        return False
    
    if index == len(word) - 1:
        return True
    
    visited.add((r, c))

    for d in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        if search(board, r + d[0], c + d[1], visited, index + 1, word):
            return True

    visited.remove((r, c)) # backtrack

    return False


def exists(board: list[list], word):
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            visited = set()
            if search(board, r, c, visited, 0, word):
                return True

    return False


if __name__ == '__main__':
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    assert exists(board, 'ABCCED') == True
    assert exists(board, 'SEE') == True
    assert exists(board, 'ABCB') == False

'''
The worst-case time complexity of this solution is O(MN * 4^L) where L is the length of the word and M and N are the dimensions of the board.
'''