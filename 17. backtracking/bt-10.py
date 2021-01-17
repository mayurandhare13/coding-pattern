'''
Given a 2D board and a word, find if the word exists in the grid.
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

def word_exists(original_board, word):
    
    def backtrack(row, col, word):
        if len(word) == 0:
            return True
        
        # Check the current status, before jumping into backtracking
        if row < 0 or row == ROWS or col < 0  or col == COLS \
            or board[row][col] != word[0]:
            return False

        # mark the choice before exploring further (visited cell)
        board[row][col] = '#'
        for rowOffset, colOffset in directions:
            if backtrack(row + rowOffset, col + colOffset, word[1:]):
                return True
        
        # revert the marking
        board[row][col] = word[0]

        # tried all direction and did not find match
        return False

    board = [r[:] for r in original_board]
    ROWS = len(board)
    COLS = len(board[0])
    # going clockwise : 0:'up', 1:'right', 2:'down', 3:'left'
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for row in range(ROWS):
        for col in range(COLS):
            if backtrack(row, col, word):
                return True
    
    return False


if __name__ == "__main__":
    board = [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ]
    print("ABCCED exists: ", word_exists(board, "ABCCED"))
    print("SEE exists: ", word_exists(board, "SEE"))
    print("ABCB: ", word_exists(board, "ABCB"))
