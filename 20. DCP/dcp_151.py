from collections import deque

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def _bounds(matrix: list[list], r, c):
    rows = len(matrix)
    cols = len(matrix[0])

    return  0 <= r < rows and 0 <= c < cols


def floodfillDFS(matrix: list[list], coord, color, visited=None):
    if not visited:
        visited = set()

    visited.add(coord)

    R, C = coord
    prevColor = matrix[R][C]

    matrix[R][C] = color

    for dir in directions:
        r, c = R + dir[0], C + dir[1]

        if _bounds(matrix, r, c) and matrix[r][c] == prevColor and \
            (r, c) not in visited:
            floodfillDFS(matrix, (r, c), color, visited)


def floodfillBFS(matrix: list[list], coord, color):
    visited = set()
    queue = deque()
    R, C = coord
    prevColor = matrix[R][C]
    queue.append(coord)

    while queue:
        R, C = queue.popleft()
        matrix[R][C] = color
        visited.add((R, C))

        for dir in directions:
            r, c = R + dir[0], C + dir[1]

            if _bounds(matrix, r, c) and matrix[r][c] == prevColor and \
                (r, c) not in visited:
                queue.append((r, c))


if __name__ == '__main__':

    matrix = [['B', 'B', 'W'],
            ['W', 'W', 'W'],
            ['W', 'W', 'W'],
            ['B', 'B', 'B']]

    floodfillBFS(matrix, (2, 2) ,'G')

    assert matrix == \
        [['B', 'B', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['B', 'B', 'B']]

# O(V + E) time and O(V) space