'''
The n-queens puzzle is the problem of placing n queens on an `nxn` chessboard such that no two queens attack each other.

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
---
HINT

0 | 1 | 2 | 3
1 | 2 | 3 | 4
2 | 3 | 4 | 5
3 | 4 | 5 | 6
^i + j (hill)

0 | -1| -2 | -3
1 | 0 | -1 | -2
2 | 1 |  0 | -1
3 | 2 |  1 | 0
^i - j (dale)
'''

def solveNQueens(n):

    def could_place(row, col):
        # basically if queen is not placed then returns `not (0 + 0 + 0) --> True`
        return not (cols[col] + hill_diagonal[row + col] + dale_diagonal[row - col])

    def place_queen(row, col):
        queens.add((row, col))
        cols[col] = 1

        # to set queen's presence in one of diagonal
        hill_diagonal[row + col] = 1
        dale_diagonal[row - col] = 1

    def remove_queen(row, col):
        queens.remove((row, col))
        cols[col] = 0
        hill_diagonal[row + col] = 0
        dale_diagonal[row - col] = 0
    
    def add_solution():
        solution = []
        for _, col in sorted(queens):
            # if n = 9, col = 3 --> (- - -) Q (- - - - -) 
            solution.append(' - ' * col + 'Q' + ' - ' * (n - col - 1))
        output.append(solution)

    def backtrack(row = 0):
        for col in range(n):
            if could_place(row, col):
                place_queen(row, col)
                if row + 1 == n:
                    add_solution()
                else:
                    backtrack(row + 1)
                remove_queen(row, col)

    output = []
    queens = set()
    cols = [0] * n
    hill_diagonal = [0] * (2*n - 1)
    dale_diagonal = [0] * (2*n - 1)

    backtrack()
    return output

if __name__ == "__main__":
    print('N Queens with 4 blocks')
    output = solveNQueens(4)
    for r in output:
        print(r)
    
    print('N Queens with 6 blocks')
    output = solveNQueens(6)
    for r in output:
        print(r)
