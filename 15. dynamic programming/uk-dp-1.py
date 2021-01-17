'''
Unbounded Knapsack

Here `static` is profits. use them as ROWS.
and `dynamic`, all possible values of `capacity` will be COLUMNS
'''

def solve_knapsack_handler(dp, profits, weights, capacity, index):
    if capacity <= 0 or index >= len(profits):
        return 0
    
    if dp[index][capacity] == -1:
        profit1 = 0
        if weights[index] <= capacity:
            profit1 = profits[index] + solve_knapsack_handler(
                                            dp, profits, weights, capacity - weights[index], index
                                        )
        
        profit2 = solve_knapsack_handler(
                        dp, profits, weights, capacity, index + 1
                    )

        dp[index][capacity] =  max(profit1, profit2)

    return dp[index][capacity]


def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return solve_knapsack_handler(dp, profits, weights, capacity, 0)


if __name__ == "__main__":
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))
