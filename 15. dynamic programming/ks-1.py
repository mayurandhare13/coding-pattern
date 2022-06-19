'''
Given the weights and profits of 'N' items, we are asked to put these items in a knapsack which has a capacity 'C'. The goal is to get the maximum profit out of the items in the knapsack. Each item can only be selected once, as we don't have multiple quantities of any item.

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
Output: 10
'''

def solve_knapsack_handler(profits, weights, capacity, currentIdx):
    # base case
    if (currentIdx < 0 or currentIdx >= len(profits)):
        return 0

    # choose the element at current index
    # make recursive call
    profit1 = 0
    if weights[currentIdx] <= capacity:
        profit1 = profits[currentIdx] + \
                    solve_knapsack_handler(profits, weights, capacity-weights[currentIdx], currentIdx+1)
    
    # do not choose
    profit2 = solve_knapsack_handler(profits, weights, capacity, currentIdx+1)
    
    return max(profit1, profit2)

def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_handler(profits, weights, capacity, 0)


if __name__ == "__main__":
    print(solve_knapsack([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
