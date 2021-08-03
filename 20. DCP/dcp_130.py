from math import inf


# O(nk) time
def maxProfit(k, prices):
    n = len(prices)

    dp = [[0 for _ in range(n)] for _ in range(k + 1)]

    for i in range(k + 1):
        dp[i][0] = 0
    
    for j in range(n):
        dp[0][j] = 0
    
    for i in range(1, k + 1):
        maxSoFar = -inf

        for j in range(1, n):
                                    # prev profit     -      prev buy
            maxSoFar = max(maxSoFar, dp[i - 1][j - 1] - prices[j - 1])

            # + sell today --> today sell - prev buy + prev profit
            dp[i][j] = max(dp[i][j - 1], maxSoFar + prices[j])

    return dp[k][-1]


if __name__ == '__main__':
    assert maxProfit(2, [5, 2, 4, 0, 1]) == 3
