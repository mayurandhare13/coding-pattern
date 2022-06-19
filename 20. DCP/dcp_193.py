def maxProfit(prices: list, fee: int):
    cash = 0            # sell
    hold = -prices[0]   # buy

    for i in range(1, len(prices)):
        # max(cash, sell stock instead)
        cash = max(cash, hold + prices[i] - fee)

        # max(buy, buy new stock instead)
        hold = max(hold, cash - prices[i])

    return cash


def maxProfit2(prices: list, fee: int):
    profit = 0
    minimum = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < minimum:
            minimum = prices[i]

        elif prices[i] > minimum + fee:
            profit += prices[i] - minimum - fee
            minimum = prices[i] - fee

    return profit


if __name__ == '__main__':
    assert maxProfit2([1, 3, 2, 8, 4, 10], 2) == 9
