def spiralMatrix(matrix: list[list]) -> list:
    res = []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    total = len(matrix) * len(matrix[0])

    while len(res) < total:
        # left -> right
        for i in range(left, right+1):
            res.append(matrix[top][i])

        top += 1

        # top -> bottom
        for j in range(top, bottom+1):
            res.append(matrix[j][right])

        right -= 1

        # right -> left
        if top <= bottom:
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])

        bottom -= 1

        if left <= right:
            # bottom -> top
            for j in range(bottom, top-1, -1):
                res.append(matrix[j][left])

        left += 1

    return res


if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    assert spiralMatrix(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7]
