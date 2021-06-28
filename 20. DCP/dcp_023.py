from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def exploreNeighbors(board: list[list], queue: deque, visited: set, x, y):
    for r, c in directions:
        newX = r + x
        newY = c + y
        if newX < 0 or newY < 0:
            continue

        if newX >= len(board) or newY >= len(board[0]):
            continue

        if board[newX][newY] == True:
            continue

        if (newX, newY) in visited:
            continue

        queue.append((newX, newY))
        visited.add((newX, newY))


def shortestPathMaze(board: list[list], srcX, srcY, destX, destY):
    rows = len(board)
    cols = len(board[0])

    queue = deque()
    visited = set()

    queue.append((srcX, srcY))
    visited.add((srcX, srcY))
    moveCount = 0

    while queue:
        levelSize = len(queue)

        while levelSize > 0:
            x, y = queue.popleft()
            if x == destX and y == destY:
                return moveCount

            exploreNeighbors(board, queue, visited, x, y)
            levelSize -= 1

        moveCount += 1

    return -1


if __name__ == '__main__':
    board = [
            [False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]
        ]

    assert shortestPathMaze(board, 3, 0, 0, 0) == 7
