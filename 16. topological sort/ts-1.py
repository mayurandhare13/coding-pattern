'''
Given a directed graph, find the topological ordering of its vertices.

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
'''

from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder
    
    # 1. initialize the graph
    inDegrees = {i:0 for i in range(vertices)}  # count incoming edges
    graph = {i:[] for i in range(vertices)}     # adjacency list graph

    # 2. build graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)         # put child in parent list
        inDegrees[child] += 1               # increment child's indegree
    
    # 3. find all sources
    sources = deque()
    for key in inDegrees:
        if inDegrees[key] == 0:
            sources.append(key)

    # 4. for each sources, add to the list, decrement child's indegree
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegrees[child] -= 1
            if inDegrees[child] == 0:
                sources.append(child)
    
    # topological sort is not possible when graph has `cycle`
    return sortedOrder if len(sortedOrder) == vertices else []



if __name__ == "__main__":
    print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    print(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    print(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))


'''
Similar:
Q:- Find if a given Directed Graph has a cycle in it or not.
If we can't determine the topological ordering of all the vertices of a directed graph, the graph has a cycle in it.
'''
