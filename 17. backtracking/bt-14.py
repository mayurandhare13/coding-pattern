'''
Given an undirected graph represented as an adjacency matrix and an integer k, determine whether each node in the graph can be colored such that no two adjacent nodes share the same color using at most k colors.
'''

'''
O(k^N) time and O(k) space, where N is the number of vertices, since we’re iterating over k colors and we are backtracking over N vertices.
'''

def isValid(graph: list[list], colors: list):
    lastVertex, lastColor = len(colors) - 1, colors[-1]
    
    coloredVertices = [
        i for i, hasEdge in enumerate(graph[lastVertex])
        if hasEdge and i < lastVertex
    ]

    for nei in coloredVertices:
        if colors[nei] == lastColor:
            return False

    return True


def colorable(graph, k, colors = []):
    if len(colors) == len(graph):
        print(colors)
        return True
    
    for i in range(k):
        colors.append(i)
        if isValid(graph, colors):
            if colorable(graph, k, colors):
                return True
        colors.pop()

    return False


if __name__ == '__main__':
    graph = [
        [ 0, 1, 1, 1 ],
        [ 1, 0, 1, 0 ],
        [ 1, 1, 0, 1 ],
        [ 1, 0, 1, 0 ],
    ]

    print(colorable(graph, 3))
