'''
Coin Change
Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

Denominations: {1,2,3}
Total amount: 5
Output: 5
Explanation: There are five ways to make the change for '5', here are those ways:
{1,1,1,1,1} 
{1,1,1,2} 
{1,2,2}
{1,1,3}
{2,3}
'''

def coin_change_handler(denominations, amount, index):
    if amount == 0:
        return 1
        
    if index >= len(denominations):
        return 0

    count1 = 0
    if denominations[index] <= amount:
        count1 = coin_change_handler(
                        denominations, amount - denominations[index], index)
    
    count2 = coin_change_handler(denominations, amount, index + 1)

    return count1 + count2


def coin_change(denominations, amount):
    return coin_change_handler(denominations, amount, 0)


if __name__ == "__main__":
    print(coin_change([1, 2, 3], 5))
