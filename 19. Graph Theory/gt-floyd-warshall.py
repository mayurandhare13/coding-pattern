import math

class FloydWarshall:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.dp = [[None for _ in range(self.n)] for _ in range(self.n)]
        self.next = [[None for _ in range(self.n)] for _ in range(self.n)]
        self.isSolved = False
        self.NEGATIVE_CYCLE = -1


        for i in range(self.n):
            for j in range(self.n):
                if matrix[i][j] != math.inf:
                    self.next[i][j] = j              # reconstructing path
                self.dp[i][j] = matrix[i][j]


    def runFloydWarshall(self):
        if self.isSolved:
            return
        
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]
                        self.next[i][j] = self.next[i][k]
        

        # second passs to detect -ve cycle
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = -math.inf
                        self.next[i][j] = self.NEGATIVE_CYCLE
        
        self.isSolved = True


    def reconstructPath(self, start, end):
        self.runFloydWarshall()

        path = []
        # path does not exists
        if self.dp[start][end] == math.inf:
            return path

        at = start        
        while at != end:
            if at == self.NEGATIVE_CYCLE:
                path.clear()
                return None
            path.append(at)
            at = self.next[at][end]
        
        if self.next[at][end] == self.NEGATIVE_CYCLE:
            path.clear()
            return None
        
        path.append(end)

        return path

    
if __name__ == "__main__":
    n = 7
    m = [[math.inf for _ in range(n)] for _ in range(n)]
    
    for i in range(len(m)):
        m[i][i] = 0
    
    m[0][1] = 2
    m[0][2] = 5
    m[0][6] = 10
    m[1][2] = 2
    m[1][4] = 11
    m[2][6] = 2
    m[6][5] = 11
    m[4][5] = 1
    m[5][4] = -2

    obj = FloydWarshall(m)
    obj.runFloydWarshall()

    print("Shortest path costs")

    for i in range(n):
        for j in range(n):
            print(f"node {i} -> {j} == {obj.dp[i][j]}")

    print("Shortest Path")
    for i in range(n):
        for j in range(n):
            path = obj.reconstructPath(i, j)
            path_str = ''
            if path is None:
                path_str = "\u221E solutions! (negative cycle)"
            elif len(path) == 0:
                path_str = "No route exists."
            else:
                for node in path:
                    path_str += " -> " + str(node)

            print(f"node {i} to {j} == {path_str}")
