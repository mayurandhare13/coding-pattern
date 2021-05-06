from collections import defaultdict

class EulerianPath:
    def __init__(self, graph):
        self.graph = graph

        # graph edges are 1-index
        self.N = len(graph) + 1

        self.edgeCount = 0
        self.inDegree = [0] * self.N
        self.outDegree = [0] * self.N
        self.path = []


    def countDegrees(self):
        for fr in range(self.N):
            for to in self.graph[fr]:
                self.outDegree[fr] += 1
                self.inDegree[to] += 1
                self.edgeCount += 1
        

    def isPathExists(self):
        if self.edgeCount == 0:
            return False

        startNode = endNode = 0

        for i in range(self.N):
            if self.outDegree[i] - self.inDegree[i] > 1 or self.inDegree[i] - self.outDegree[i] > 1:
                return False
            
            elif self.outDegree[i] - self.inDegree[i] == 1:
                startNode += 1
            
            elif self.inDegree[i] - self.outDegree[i] == 1:
                endNode += 1
        
        return startNode == 0 and endNode == 0 or \
            (startNode == 1 and endNode == 1)


    def findStartNode(self):
        start = 0
        for i in range(self.N):
            # unique starting node
            if self.outDegree[i] - self.inDegree[i] == 1:
                return i

            # start at a node with outgoing edge
            if self.outDegree[i] > 0:
                start = i
        
        return start


    def dfs(self, at):
        while self.outDegree[at] > 0:
            self.outDegree[at] -= 1
            nextNode = self.graph[at][self.outDegree[at]]
            self.dfs(nextNode)
        
        self.path.append(at)


    def getEulerianPath(self):
        self.countDegrees()
        if not self.isPathExists():
            print ('Path does not exists')
            return
        
        self.dfs(self.findStartNode())
        self.path.reverse()
        # check if all the edges of graph are visited
        # there could be a case graph is disconnected, return None
        if len(self.path) != self.edgeCount + 1:
            return None

        return self.path


if __name__ == '__main__':
    vertices = 7
    graph = defaultdict(list)
    graph[1].append(2)
    graph[1].append(3)
    graph[2].append(2)
    graph[2].append(4)
    graph[2].append(4)
    graph[3].append(1)
    graph[3].append(2)
    graph[3].append(5)
    graph[4].append(3)
    graph[4].append(6)
    graph[5].append(6)
    graph[6].append(3)

    ep = EulerianPath(graph)
    path = ep.getEulerianPath()
    print(path)
