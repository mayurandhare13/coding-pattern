def buildGraph(numNodes, edges):
    graph = {i:[] for i in range(numNodes)}

    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    return graph


def hasCycle(at, graph, visited, recursiveStack, order):
    visited[at] = True
    recursiveStack[at] = True

    edges = graph[at]
    if edges:
        for to in edges:
            if not visited[to]:
                if hasCycle(to, graph, visited, recursiveStack, order):
                    return True
            elif recursiveStack[to]:
                return True
    
    order.append(at)
    recursiveStack[at] = False
    return False


def topSort(graph):
    N = len(graph)
    order = []
    visited = [False] * N
    recursiveStack = [False] * N

    for at in range(N):
        if not visited[at]:
            if hasCycle(at, graph, visited, recursiveStack, order):
                return None
    
    return order[::-1]


def largestValuePathUtil(letters, graph, order):
    zIndex = ord('Z') + 1
    dp = [[0] * zIndex for _ in range(len(graph))]

    for node in graph:
        dp[node][ord(letters[node])] += 1

    maxPath = 0

    for node in order:
        for adj in graph[node]:
            for i in range(zIndex):
                dp[adj][i] = max(dp[adj][i], dp[node][i])

            dp[adj][ord(letters[adj])] = 1 + dp[node][ord(letters[adj])]
            maxPath = max(maxPath, dp[adj][ord(letters[adj])])

    return maxPath


def largestValuePath(word, edges):
    graph = buildGraph(len(word), edges)

    order = topSort(graph)
    if not order:
        return -1

    return largestValuePathUtil(word, graph, order)


if __name__ == '__main__':
    edges = [
        [0, 1], [0, 2],
        [2, 3], [3, 4]
    ]
    # [0, 2, 3, 4], (A, A, C, A)
    maxFreq = largestValuePath('ABACA', edges)
    print(maxFreq)
