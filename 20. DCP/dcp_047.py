import math

def getMaxProfit(prices: list) -> int:
    if not prices or len(prices) < 2:
        return
    
    minPrice = math.inf
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price

        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    
    return maxProfit


if __name__ == '__main__':
    print(getMaxProfit([9, 11, 8, 5, 7, 10]))
    print(getMaxProfit([7, 1, 5, 3, 6, 4]))
