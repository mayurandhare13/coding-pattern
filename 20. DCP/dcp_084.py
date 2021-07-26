def dfs(grid: list[list], r, c):
    rows = len(grid)
    cols = len(grid[0])

    if r < 0 or r >= rows \
        or c < 0 or c >= cols \
            or grid[r][c] == 0:
        return
    
    grid[r][c] = 0
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)


def numberIslands(grid: list[list]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    numOfIslands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                numOfIslands += 1
                dfs(grid, r, c)
    
    return numOfIslands


if __name__ == '__main__':
    worldMap = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    assert numberIslands(worldMap) == 4
    # O(M×N) time
