def solve_knapsack_handler(profits, weights, capacity, currentIdx, dp):
    # base case
    if currentIdx < 0 or currentIdx >= len(profits):
        return 0
    
    # if we already solved the similar problem, return result
    if dp[currentIdx][capacity] != -1:
        return dp[currentIdx][capacity]

    profit1 = 0
    if weights[currentIdx] <= capacity:
        profit1 = profits[currentIdx] + \
            solve_knapsack_handler(profits, weights, capacity - weights[currentIdx], currentIdx + 1, dp)

    profit2 = solve_knapsack_handler(profits, weights, capacity, currentIdx + 1, dp)

    dp[currentIdx][capacity] = max(profit1, profit2)
    return dp[currentIdx][capacity]

def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity + 1)] for i in range(len(weights))]
    return solve_knapsack_handler(profits, weights, capacity, 0, dp)


if __name__ == "__main__":
    print(solve_knapsack([4, 5, 3, 7], [2, 3, 1, 4], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
