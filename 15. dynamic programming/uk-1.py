'''
Unbounded Knapsack

Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. We can assume an infinite supply of item quantities; therefore, each item can be selected multiple times.
'''

def solve_knapsack_handler(profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0
    
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = profits[index] + solve_knapsack_handler(
                                        profits, weights, capacity - weights[index], index
                                    )
    
    profit2 = solve_knapsack_handler(
                    profits, weights, capacity, index + 1
                )

    return max(profit1, profit2)


def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_handler(profits, weights, capacity, 0)


if __name__ == "__main__":
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))
