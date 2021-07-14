# O(2^n) time
def numberOfPaths(m, n):
    if m < 1 or n < 1:
        return 0

    if m == 1 and n == 1:
        return 1

    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)


# O(n^2) space
def uniquePaths(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[m-1][n-1]


# O(n) space
# first draw table, you can find optimization on above solution
def uniquePathsOpt(m, n):
    dp = [1 for _ in range(n)]

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]

    return dp[-1]


if __name__ == '__main__':

    assert numberOfPaths(5, 5) == 70
    assert numberOfPaths(2, 3) == 3

    assert uniquePaths(5, 5) == 70
    assert uniquePaths(2, 3) == 3

    assert uniquePathsOpt(5, 5) == 70
    assert uniquePathsOpt(2, 3) == 3
