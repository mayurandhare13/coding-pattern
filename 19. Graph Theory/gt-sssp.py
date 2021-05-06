
# O(V + E)

class Edge(object):

    def __init__(self, f = None, t = -1, c = -1):
        self._from = f
        self._to = t
        self._cost = c


class TopologicalSort(object):

    def dfs(self, at, index, graph, visited, order):
        visited[at] = True

        edges = graph.get(at, None)
        if edges:
            for edge in edges:
                if edge._to and not visited[edge._to]:
                    index = self.dfs(edge._to, index, graph, visited, order)
        
        order[index] = at
        return index - 1


    def topSort(self, graph, N):
        order = [None] * N
        visited = [False] * N

        i = N - 1
        for at in range(N):
            if not visited[at]:
                i = self.dfs(at, i, graph, visited, order)

        return order

    
    def dagShortestPath(self, graph, N, startVertex):
        order = self.topSort(graph, N)
        dist = [None] * N
        dist[startVertex] = 0

        for nodeIndex in order:
            if dist[nodeIndex] is not None:
                edges = graph.get(nodeIndex, None)
                if edges:
                    for edge in edges:
                        newDist = dist[nodeIndex] + edge._cost
                        if not dist[edge._to]:
                            dist[edge._to] = newDist
                        else:
                            dist[edge._to] = min(dist[edge._to], newDist)
        
        return dist


if __name__ == "__main__":
    N = 7
    graph = {
        0 : [Edge(0, 1, 3), Edge(0, 2, 2), Edge(0, 5, 3)],
        1 : [Edge(1, 3, 1), Edge(1, 2, 6)],
        2 : [Edge(2, 3, 1), Edge(2, 4, 10)],
        3 : [Edge(3, 4, 5)],
        5 : [Edge(5, 4, 7)],
        6 : [Edge(6)]
    }

    obj = TopologicalSort()
    order = obj.topSort(graph, N)
    print(order)

    distance = obj.dagShortestPath(graph, N, 0)
    print(distance)
    print(f"{0} to {4} -> {distance[4]}")

    distance = obj.dagShortestPath(graph, N, 2)
    print(distance)
    print(f"{2} to {4} -> {distance[4]}")
