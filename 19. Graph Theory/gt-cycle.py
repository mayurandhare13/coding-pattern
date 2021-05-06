class Graph:
    def __init__(self, N):
        self.N = N
        self.adjList = [[] for _ in range(N)]

    def addEdge(self, source, dest):
        self.adjList[source].append(dest)

    def isCycle(self):
        visited = [False] * self.N

        # stack[] is used to keep track of VISITING vertices during DFS from particular vertex
        recursiveStack = [False] * self.N

        # do DFS on each node
        for i in range(self.N):
            if self.isCycleUtil(i, visited, recursiveStack):
                return True
        
        return False
    
    def isCycleUtil(self, node, visited, recursiveStack):
        visited[node] = True
        recursiveStack[node] = True

        for adj in self.adjList[node]:
            if not visited[adj]:
                if self.isCycleUtil(adj, visited, recursiveStack):
                    return True

            elif recursiveStack[adj]:
                return True
        
        # if reached here means cycle has not found in DFS from this vertex
        recursiveStack[node] = False
        return False


if __name__ == '__main__':
    vertices = 5
    graph = Graph(vertices)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(0, 3)
    graph.addEdge(3, 2)
    graph.addEdge(3, 4)
    graph.addEdge(2, 4)
    graph.addEdge(4, 1) # creates cycle
    
    result = graph.isCycle()
    print("is Cycle present: ", result)
    '''
            0
           /  \
          1    3
         /^\ / \
        |   2-->4
         \______|
        
        1 --> 2 --> 4 --> 1
    '''