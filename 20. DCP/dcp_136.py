def rectangleArea(cache: list):
    N = len(cache)
    area = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            area = max(area, min(cache[i:j]) * (j - i))
    
    return area


def largestRectangle(matrix: list[list]):
    cache = [0] * len(matrix)
    maxArea = 0
    for row in matrix:
        for i, val in enumerate(row):
            if val == 0:
                cache[i] = 0
            else:
                cache[i] += 1

        maxArea = max(maxArea, rectangleArea(cache))

    return maxArea


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 0]
    ]

    # O(MN^3)
    assert largestRectangle(matrix) == 4
