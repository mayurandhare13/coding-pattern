'''
Rod Cutting
Given a rod of length 'n', we are asked to cut the rod and sell the pieces in a way that will maximize the profit. We are also given the price of every piece of length 'i' where `1 <= i <= n`.

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5
'''

def maximize_rod_profit_handler(lengths, prices, rod_length, index):
    if rod_length <= 0 or index >= len(prices):
        return 0

    profit1 = 0
    if lengths[index] <= rod_length:
        profit1 = prices[index] + maximize_rod_profit_handler(
                                    lengths, prices, rod_length - lengths[index], index
                                )

    profit2 = maximize_rod_profit_handler(lengths, prices, rod_length, index + 1)
    
    return max(profit1, profit2)


def maximize_rod_profit(lengths, prices, rod_length):
    return maximize_rod_profit_handler(lengths, prices, rod_length, 0)


if __name__ == "__main__":
    print(maximize_rod_profit([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
