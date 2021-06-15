def coinGame(arr):
    N = len(arr)
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # we only fill upper part of matrix
    for g in range(N):
        i = 0
        for j in range(g, N):
            if g == 0:              # 1st diagonal
                dp[i][j] = arr[i]
            
            elif g == 1:            # 2nd diagonal
                dp[i][j] = max(arr[i], arr[j])
            
            else:                   # remaining
                # choose i --> opponent can choose i+1, j
                v1 = arr[i] + min(dp[i + 2][j], dp[i + 1][j - 1])
                # choose j --> opponent can choose i, j-1
                v2 = arr[j] + min(dp[i + 1][j - 1], dp[i][j - 2])

                dp[i][j] = max(v1, v2)
            
            i += 1
    

    print(dp[0][N - 1])


if __name__ == '__main__':
    arr1 = [20, 30, 2, 10]
    coinGame(arr1)

    arr2 = [6, 9, 1, 2, 16, 8]
    coinGame(arr2)
