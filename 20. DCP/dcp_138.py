# O(N) time & space
def minCoins(demoninations: list, amount):
    dp = [0] * (amount + 1)

    for d in demoninations:
        if d < len(dp):
            dp[d] = 1
    
    for i in range(1, amount + 1):
        dp[i] = min(1 + dp[i - d] for d in demoninations if i - d >= 0)
    
    return dp[amount]


if __name__ == '__main__':
    assert minCoins([1, 5, 10], 16) == 3
