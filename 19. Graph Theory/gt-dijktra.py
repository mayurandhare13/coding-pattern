class Edge:
    def __init__(self, f = None, t = -1, c = -1):
        self._from = f
        self._to = t
        self._cost = c


class Node:
    def __init__(self, id, val):
        self.id = id
        self.val = val
    
    def __lt__(self, other):
        return self.val < other.val


from heapq import *
import math

class Dijkstra:
    def __init__(self, N, graph):
        self.N = N
        self.graph = graph
        self.dist = []
        self.prev = []

    def dijkstra(self, start, end):
        visited = [False] * self.N
        self.prev = [None] * self.N
        self.dist = [math.inf] * self.N

        queue = []
        heappush(queue, Node(start, 0))
        self.dist[start] = 0

        while queue:
            node = heappop(queue)
            visited[node.id] = True
            if self.dist[node.id] < node.val:
                continue

            edges = self.graph.get(node.id)
            if edges:
                for edge in edges:
                    if not visited[edge._to]:
                        newDist = self.dist[node.id] + edge._cost
                        if newDist < self.dist[edge._to]:
                            self.dist[edge._to] = newDist
                            self.prev[edge._to] = node.id
                            heappush(queue, Node(edge._to, newDist))
        
            if node.id == end:
                return self.dist[end]
        
        return math.inf


    def reconstructPath(self, start, end):
        distance = self.dijkstra(start, end)
        print("distance: ", distance)

        path = []
        if distance == math.inf:
            return path
        
        at = end
        while at:
            path.append(at)
            at = self.prev[at]
        
        path.reverse()

        return path


if __name__ == "__main__":
    N = 5
    graph = {
        0 : [Edge(0, 1, 4), Edge(0, 2, 1)],
        1 : [Edge(1, 3, 1)],
        2 : [Edge(2, 1, 2), Edge(2, 3, 5)],
        3 : [Edge(3, 4, 3)],
    }

    obj = Dijkstra(5, graph)
    # distance = obj.dijkstra(0)
    # print(distance)

    path = obj.reconstructPath(0, 4)
    print(path)
