'''
Tasks Scheduling Order (medium)

There are 'N' tasks, labeled from '0' to 'N-1'. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 
'''

from collections import deque


def find_order(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return sortedOrder

    # 1. initilize indegrees and graph
    indegrees = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    # 2. build graph
    for task in prerequisites:
        parent, child = task[0], task[1]
        graph[parent].append(child)
        indegrees[child] += 1
    
    # 3. find initial sources
    sources = deque()
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)

    # 4. iterate over all vertices
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sources.append(child)


    return sortedOrder if len(sortedOrder) == tasks else []


if __name__ == "__main__":
    print(find_order(3, [[0, 1], [1, 2]]))
    print(find_order(3, [[0, 1], [1, 2], [2, 0]]))
    print(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
    print(find_order(3, [[0, 1],[1, 2],[2, 0]]))
