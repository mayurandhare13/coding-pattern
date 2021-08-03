# O(MN) both space and time
def collectCoins(matrix: list[list], r=0, c=0, cache=dict()):
    rows = len(matrix)
    cols = len(matrix[0])

    isBottom = r == rows - 1
    isRight = c == cols - 1

    if (r, c) not in cache:
        if isBottom and isRight:
            result = matrix[r][c]

        elif isBottom:
            result = matrix[r][c] + collectCoins(matrix, r, c + 1, cache)

        elif isRight:
            result = matrix[r][c] + collectCoins(matrix, r + 1, c, cache)

        else:
            result = matrix[r][c] + \
                max (
                    collectCoins(matrix, r + 1, c, cache),
                    collectCoins(matrix, r, c + 1, cache)
                )


        cache[(r, c)] = result

    return cache[(r, c)]


if __name__ == '__main__':
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]
    ]

    assert collectCoins(matrix) == 12
