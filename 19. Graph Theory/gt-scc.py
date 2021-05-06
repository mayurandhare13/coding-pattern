class Tarjan:
    def __init__(self, graph):
        self.graph = graph
        self.N = len(graph)
        self.ids = [-1] * self.N
        self.lows = [-1] * self.N
        self.onStack = [False] * self.N
        self.stack = []
        self.scc = [-1] * self.N

        self.SCC_COUNTER = 0
        self.ID = 0


    def dfs(self, at):
        self.ids[at] = self.ID
        self.lows[at] = self.ID
        self.ID += 1

        self.onStack[at] = True
        self.stack.append(at)

        for to in self.graph[at]:
            if self.ids[to] == -1:
                self.dfs(to)
            
            if self.onStack[to]:
                self.lows[at] = min(self.lows[at], self.lows[to])
        
        # on recursion callback, we're at root node
        # start of SCC
        if self.ids[at] == self.lows[at]:
            while self.stack:
                node = self.stack.pop()
                self.onStack[node] = False

                # set the start of the SCC to all nodes in that SCC
                self.scc[node] = at

                if node == at:
                    break
        
        self.SCC_COUNTER += 1


    def tarjansScc(self):

        for i in range(self.N):
            if self.ids[i] == -1:
                self.dfs(i)
        
        return self.scc


graph = {
    0 : [1],
    1 : [2],
    2 : [0],
    3 : [4, 7],
    4 : [5],
    5 : [0, 6],
    6 : [0, 2, 4],
    7 : [3, 5]
}
solver = Tarjan(graph)

sccs = solver.tarjansScc()
print(sccs)