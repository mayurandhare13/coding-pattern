'''
All Paths From Source to Target
Given a DAG of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

NOTE: 0 -> 1, 0 -> 2, 1 & 2 parent of 3
'''

from collections import deque


def allPathSourceTarget(graph):
    target = len(graph) - 1
    result = []

    def backtrack(currentNode, path):
        if currentNode == target:
            result.append(list(path))
            return
        
        for node in graph[currentNode]:
            path.append(node)
            backtrack(node, path)
            path.pop()


    path = deque([0]) # start from sources | we want 0 as the beginning
    backtrack(0, path)
    return result


if __name__ == "__main__":
    print(allPathSourceTarget([[1,2],[3],[3],[]]))              # target = 3
    print(allPathSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))    # target = 4
    print(allPathSourceTarget([[1],[]]))                        # target = 1
    