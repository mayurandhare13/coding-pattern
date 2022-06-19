'''
similar to the N queens problem (#38) or the flight itinerary problem (#41). The basic idea is this:

For every possible square, initialize a knight there, and then:
Try every valid move from that square.
Once we’ve hit every single square, we can add to our count.
'''

'''
This takes O(N * N) space and potentially O(8^(N^2)) time.
Since at each step we have potentially 8 moves to check,
and we have to do this for each square.
'''


def isValid(move, board, n):
    r, c = move
    return 0 <= r < n and 0 <= c < n and board[r][c] is False


def validMoves(board, r, c, n):
    deltas = [
        (2, 1),
        (-2, 1),
        (2, -1),
        (-2, -1),
        (1, 2),
        (-1, 2),
        (1, -2),
        (-1, -2)
    ]

    allMoves = [ (r + rDelta, c + cDelta) 
                    for rDelta, cDelta in deltas
            ]

    return [ move
        for move in allMoves if isValid(move, board, n)
    ]


def knightTourHelper(board, tour, n):
    if len(tour) == n * n:
        return 1
    
    count = 0
    lastR, lastC = tour[-1]

    for r, c in validMoves(board, lastR, lastC, n):
        tour.append((r, c))
        board[r][c] = True     # <-- to mark visited
        
        count += knightTourHelper(board, tour, n)

        tour.pop()
        board[r][c] = False
    
    return count


def knightTour(n) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            board = [[False for _ in range(n)] for _ in range(n)]
            board[i][j] = True
            count += knightTourHelper(board, [(i, j)], n)

    return count


if __name__ == '__main__':
    print(knightTour(8))
    assert knightTour(1) == 1
    assert knightTour(2) == 0
    assert knightTour(3) == 0
    assert knightTour(4) == 0
    assert knightTour(5) == 1728
