'''
Coin Change
Static: denominations
Dynamic: total ways to get that amount sum
'''

def coin_change_handler(dp, denominations, amount, index):
    if amount == 0:
        return 1
        
    if index >= len(denominations):
        return 0

    if dp[index][amount] == -1:
        count1 = 0
        if denominations[index] <= amount:
            count1 = coin_change_handler(
                            dp, denominations, amount - denominations[index], index)
        
        count2 = coin_change_handler(dp, denominations, amount, index + 1)

        dp[index][amount] = count1 + count2
    
    return dp[index][amount]


def coin_change(denominations, amount):
    dp = [[-1 for _ in range(amount + 1)] for _ in range(len(denominations))]
    return coin_change_handler(dp, denominations, amount, 0)


if __name__ == "__main__":
    print(coin_change([1, 2, 3], 5))
