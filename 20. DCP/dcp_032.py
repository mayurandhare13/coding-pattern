# Bellman ford can find negative edges
# since our question ask us to find arbitrage with amount greater than original
# to get the edge path a -> b -> c -> d. Since we want to see if a * b * c * d > 1
# so to get the negative cycle, we can use log(a * b) = log(a) + log(b).
# take the negative log of each edge 
# -(log(a) + log(b) + log(c) + log(d)) = -log(a * b * c * d) = -log(x) < 0
# if x is greater than 1, so that’s why if we have a negative cost cycle, 
# if means that the product of the weighted edges is bigger than 1

from math import log

def arbitrage(table: list[list]) -> bool:
    graph = [[-log(edge) for edge in row] for row in table]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    
    source = 0
    n = len(graph)
    minDistance = [float('inf')] * n
    minDistance[source] = 0

    # relax edges |V - 1| edges
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if minDistance[w] > minDistance[v] + graph[v][w]:
                    minDistance[w] = minDistance[v] + graph[v][w]
    
    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if minDistance[w] > minDistance[v] + graph[v][w]:
                return True

    return False


if __name__ == '__main__':
    assert arbitrage([[1, 2], [2, 1]])
    assert not arbitrage([[1, 1], [1, 1]])