'''
Minimum Height Trees (hard) #
We are given an "undirected graph" that has characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs. Write a method to find all MHTs of the given graph and return a list of their roots.

Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
Explanation: Choosing '1' or '2' as roots give us MHTs.
'''

'''
HINT
Any node with only one edge (i.e., a leaf) can be our source and, in a stepwise fashion, we can remove all sources from the graph to find new sources. We will repeat this process until we are left with one or two nodes in the graph, which will be our answer.
'''

from collections import deque


def find_minimum_trees(nodes, edges):
    if nodes <= 0:
        return []
    
    # 1. initialize indegrees and `undirected` graph
    indegrees = {i:0 for i in range(nodes)}
    graph = {i:[] for i in range(nodes)}

    # 2. build indegrees and `undirected` graph
    for edge in edges:
        e1, e2 = edge[0], edge[1]
        indegrees[e1] += 1
        indegrees[e2] += 1
        graph[e1].append(e2)
        graph[e2].append(e1)

    # 3. find leaves | here leaf nodes (i.e single edge)
    leaves = deque()
    for key, val in indegrees.items():
        if val == 1:
            leaves.append(key)
    
    # 4. remove leaves level by level and subtract each leaves children indegees
    # repeat this until we are left with 1 or 2 nodes
    # any node which was leaf node will never root of MHT as its adjacent non leaf will always be better candidate

    totalNodes = nodes
    while totalNodes > 2:
        leavesSize = len(leaves)
        totalNodes -= leavesSize
        for i in range(leavesSize):
            leaf = leaves.popleft()
            # get children (as it is undirected graph, every node has child) to decrement their indegree
            for child in graph[leaf]:
                indegrees[child] -= 1
                if indegrees[child] == 1:
                    leaves.append(child)

    return list(leaves)


if __name__ == "__main__":
    print("roots of MHT: ", find_minimum_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]]))
    print("roots of MHT: ", find_minimum_trees(4, [[0, 1], [0, 2], [2, 3]]))
    print("roots of MHT: ", find_minimum_trees(4, [[0, 1], [1, 2], [1, 3]]))
