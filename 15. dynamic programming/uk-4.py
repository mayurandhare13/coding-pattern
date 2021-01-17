'''
MINIMUM Coin Change

Denominations: {1,2,3}
Total amount: 5
Output: 2
Explanation: We need minimum of two coins {2,3} to make a total of '5'
'''

import math


def coin_change_handler(denominations, amount, index):
    if amount == 0:
        return 0
    
    # if we don't have coin change we return max value
    # if we return 0 (like uk-3) and 1 when we found change (amount = 0)
    # then min (0, 1) -> 0, and we don't have the the solution
    if index >= len(denominations):
        return math.inf

    count1 = math.inf
    if denominations[index] <= amount:
        res = coin_change_handler(
                denominations, amount - denominations[index], index
            )
        if res != math.inf:
            count1 = 1 + res
    
    count2 = coin_change_handler(
                denominations, amount, index + 1
            )
    
    return min(count1, count2)


def coin_change(denominations, amount):
    result = coin_change_handler(denominations, amount, 0)
    return -1 if result == math.inf else result    


if __name__ == "__main__":
    print(coin_change([1, 2, 3], 5))
    print(coin_change([1, 2, 3], 11))
    print(coin_change([1, 2, 3], 7))
    print(coin_change([3, 5], 7))
