import math

graph = [
    [0, 20, 42, 25],
    [20, 0, 30, 34],
    [42, 30, 0, 10],
    [25, 34, 10, 0]
]

n = len(graph)
VISITED_ALL = (1 << n) - 1

def tsp(graph, visited, pos):
    if visited == VISITED_ALL:
        return graph[pos][0]
    
    minWeight = math.inf
    for city in range(n):
        if (1 << city) & visited:
            continue

        weight = graph[pos][city] + tsp(graph, (1 << city) | visited, city)
        minWeight = min(minWeight, weight)

    return minWeight


if __name__ == '__main__':

    ans = tsp(graph, 1, 0)
    print(f"Min weight to cover all nodes from 0th Node: {ans}")

    ans = tsp(graph, 2, 1)
    print(f"Min weight to cover all nodes from 1st Node: {ans}")

    ans = tsp(graph, 4, 2)
    print(f"Min weight to cover all nodes from 2nd Node: {ans}")

    ans = tsp(graph, 8, 3)
    print(f"Min weight to cover all nodes from 3rd Node: {ans}")
