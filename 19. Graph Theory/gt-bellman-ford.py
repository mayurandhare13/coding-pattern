class Edge:
    def __init__(self, f = None, t = -1, c = -1):
        self._from = f
        self._to = t
        self._cost = c
    
    def __str__(self):
        return f"{self._from} --> {self._to} [{self._cost}]"


import math

def bellmanFord(graph, V, start):

    dist = [math.inf] * V
    dist[start] = 0

    for i in range(V - 1):
        for j in range(len(graph)):
            for edge in graph.get(j):
                if dist[edge._from] + edge._cost < dist[edge._to]:
                    dist[edge._to] = dist[edge._from] + edge._cost

    for i in range(V - 1):
        for j in range(len(graph)):
            for edge in graph.get(j):
                if dist[edge._from] + edge._cost < dist[edge._to]:
                    dist[edge._to] = -math.inf
    
    return dist



if __name__ == "__main__":
    V = 9
    start = 0

    graph = {
        0 : [Edge(0, 1, 1)],
        1 : [Edge(1, 2, 1), Edge(1, 5, 4), Edge(1, 6, 4)],
        2 : [Edge(2, 4, 1)],
        3 : [Edge(3, 2, 1)],
        4 : [Edge(4, 3, -3)],
        5 : [Edge(5, 6, 5), Edge(5, 7, 3)],
        6 : [Edge(6, 7, 4)],
    }

    dist = bellmanFord(graph, V, start)
    for i in range(V):
        print(f"Cost: node {start} -> {i} == {dist[i]}")
