'''
Tasks Scheduling (medium)

There are 'N' tasks, labeled from '0' to 'N-1'. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2] 
'''

from collections import deque


def is_scheduling_possible(tasks, prerequisites):
    sortedOrders = []
    if tasks <= 0:
        return False
    
    # 1. initialize indegrees and graph
    indegrees = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    # 2. build a graph
    for task in prerequisites:
        parent, child = task[0], task[1]
        indegrees[child] += 1
        graph[parent].append(child)

    # 3. find all sources
    sources = deque()
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)
    
    # 4. iterate over sources
    while sources:
        vertex = sources.popleft()
        sortedOrders.append(vertex)
        for child in graph[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sources.append(child)

    return len(sortedOrders) == tasks



if __name__ == "__main__":
    print(is_scheduling_possible(3, [[0, 1], [1, 2]]))
    print(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))
    print(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
