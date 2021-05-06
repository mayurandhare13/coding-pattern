from heapq import heappush, heappop
from collections import defaultdict

class Edge:
    def __init__(self, _from, _to, cost):
        self._from = _from
        self._to = _to
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"from: {self._from}, to: {self._to}, cost: {self.cost}"


class PrimsMST:
    def __init__(self, graph):
        self.graph = graph
        self.N = len(graph)
        self.visited = [False] * self.N


    def addEdges(self, at, queue):
        self.visited[at] = True
        
        edges = self.graph[at]
        for edge in edges:
            if not self.visited[edge._to]:
                heappush(queue, edge)


    def lazyPrims(self, s = 0):
        totalEdges = self.N - 1
        edgeCount, mstCost = 0, 0
        mstEdges = [None] * totalEdges

        queue = []
        self.addEdges(s, queue)

        while queue and edgeCount != totalEdges:
            edge = heappop(queue)
            nodeIndex = edge._to

            if self.visited[nodeIndex]:
                continue
            
            mstEdges[edgeCount] = edge
            edgeCount += 1
            mstCost += edge.cost

            self.addEdges(nodeIndex, queue)

        if edgeCount != totalEdges:
            return (None, None)
        
        return (mstCost, mstEdges)


def addUndirectedEdge(graph, source, dest, cost):
    graph[source].append(Edge(source, dest, cost))
    graph[dest].append(Edge(dest, source, cost))


if __name__ == '__main__':
    graph = defaultdict(list)
    addUndirectedEdge(graph, 0, 1, 9)
    addUndirectedEdge(graph, 0, 2, 0)
    addUndirectedEdge(graph, 0, 3, 5)
    addUndirectedEdge(graph, 0, 5, 7)
    addUndirectedEdge(graph, 1, 3, -2)
    addUndirectedEdge(graph, 1, 4, 3)
    addUndirectedEdge(graph, 1, 6, 4)
    addUndirectedEdge(graph, 2, 5, 6)
    addUndirectedEdge(graph, 3, 5, 2)
    addUndirectedEdge(graph, 3, 6, 3)
    addUndirectedEdge(graph, 4, 6, 6)
    addUndirectedEdge(graph, 5, 6, 1)
    
    solver = PrimsMST(graph)
    mstCost, mstEdges = solver.lazyPrims(0)
    
    print(f"MST COST: {mstCost}")
    print("MST EDGES: ")
    for edge in mstEdges:
        print(edge)

