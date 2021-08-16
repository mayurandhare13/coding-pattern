def rotate(matrix: list[list]):
    N = len(matrix)

    # outer layer -> inner layer
    for i in range(N // 2):
        # think only j is the moving part and deduce relation
        for j in range(i, N - i - 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[N - j - 1][i]
            matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1]
            matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1]
            matrix[j][N - i - 1] = tmp


if __name__ == '__main__':
    matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    
    rotate(matrix)

    assert matrix == [[7, 4, 1],
                        [8, 5, 2],
                        [9, 6, 3]]
