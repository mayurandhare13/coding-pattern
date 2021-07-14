# To represent the colors, we can just keep a separate colors list that maps 1-to-1 with the vertices. 
# You can also convert the graph into nodes and add a color property as well.


def isValid(graph: list[list], colors: list) -> bool:
    lastVertex, lastColor = len(colors) - 1, colors[-1]

    coloredNeighbors = [ node
        for node, hasEdge in enumerate(graph[lastVertex]) 
        if hasEdge and node < lastVertex
    ]

    for nei in coloredNeighbors:
        if colors[nei] == lastColor:
            return False

    return True


def colorable(graph: list[list], k, colors=[]):
    if len(graph) == len(colors):
        print(colors)
        return True
    
    for c in range(k):
        colors.append(c)
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

    assert colorable(graph, 3) == True


# This runs in O(k^N) time and O(k) space, where N is the number of vertices.
# since we’re iterating over k colors and we are backtracking over N vertices.
