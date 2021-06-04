def numbersBetween(mat, i1, j1, i2, j2):
    num1, num2 = mat[i1][j1], mat[i2][j2]
    # small, large = (num1, num2) if num1 < num2 else (num2, num1)
    small, large = num1, num2

    count = 0
    for row in mat:
        count += len([x for x in row if (x < small or x > large)])
    
    return count


if __name__ == '__main__':
    mat = [
        [1, 3, 7, 10, 15, 20],
        [2, 6, 9, 14, 22, 25],
        [3, 8, 10, 15, 25, 30],
        [10, 11, 12, 23, 30, 35],
        [20, 25, 30, 35, 40, 45]
    ]

    print(numbersBetween(mat, 1, 1, 3, 3))

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [10, 11, 12, 13],
        [20, 21, 22, 23]
    ]
    print(numbersBetween(matrix, 1, 0, 3, 3))
