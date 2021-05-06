import math

# graph = [
#     [0, 20, 42, 25],
#     [20, 0, 30, 34],
#     [42, 30, 0, 10],
#     [25, 34, 10, 0]
# ]

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

dp = [[-1 for j in range(n)] for i in range(1 << n)]


VISITED_ALL = (1 << n) - 1

def tsp(graph, pos):
    return tspHelper(graph, 1 << pos, pos, pos)

def tspHelper(graph, visited, pos, originalPos):
    if dp[visited][pos] != -1:
        return dp[visited][pos]

    if visited == VISITED_ALL:
        return graph[pos][originalPos]
    
    minWeight = math.inf
    for city in range(n):
        if (1 << city) & visited:
            continue

        weight = graph[pos][city] + tspHelper(graph, (1 << city) | visited, city, originalPos)
        minWeight = min(minWeight, weight)

    dp[visited][pos] = minWeight
    return dp[visited][pos]


if __name__ == '__main__':

    # ans = tsp(graph, 0)
    # print(f"Min weight to cover all nodes from 0th Node: {ans}")

    # ans = tsp(graph, 1)
    # print(f"Min weight to cover all nodes from 1st Node: {ans}")

    # ans = tsp(graph, 2)
    # print(f"Min weight to cover all nodes from 2nd Node: {ans}")

    ans = tsp(graph, 3)
    print(f"Min weight to cover all nodes from 3rd Node: {ans}")
    
    # minimum weight from all of these will be all same
