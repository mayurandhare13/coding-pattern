import math


class Solution:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        self.lows = [math.inf] * self.n
        self.ids = [math.inf] * self.n
        self.visited = [False] * self.n
        self.time = 1
        self.bridges = []

    def find_bridges(self):
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i, -1)
    
        return self.bridges

    
    def dfs(self, at, parent):
        self.visited[at] = True
        self.lows[at] = self.ids[at] = self.time
        self.time += 1

        for to in self.graph[at]:
            if to == parent:
                continue
            
            if not self.visited[to]:
                self.dfs(to, at)
                # update `lows` as we came back from visiting `to`
                self.lows[at] = min(self.lows[at], self.lows[to])

                if self.lows[to] > self.ids[at]:
                    self.bridges.append([at, to])
            else:
                self.lows[at] = min(self.lows[at], self.ids[to])



if __name__ == '__main__':
    # indirected graph
    graph = {
        0 : [1, 2],
        1 : [0, 2],
        2 : [0, 1, 3, 5],
        3 : [2, 4],
        4 : [3],
        5 : [2, 6, 8],
        6 : [5, 7],
        7 : [6, 8],
        8 : [5, 7]
    }

    sol = Solution(9, graph)

    bridges = sol.find_bridges()
    print(bridges)
