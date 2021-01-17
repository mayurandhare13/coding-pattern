'''
All Tasks Scheduling Orders (hard)

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output: 
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.
'''

from collections import deque

# to find all possible orders | BACKTRACKING

def print_all_topological_sort(indegrees, graph, sources, sortedOrder):
    for vertex in sources:
        sortedOrder.append(vertex)
        sourcesNextCall = deque(sources)    # make copy of sources
        sourcesNextCall.remove(vertex)      # only remove current vertex for recursive call

        for child in graph[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sourcesNextCall.append(child)
        
        # recursive call to print ordering from remaining & new sources
        print_all_topological_sort(indegrees, graph, sourcesNextCall, sortedOrder)

        # BACKTRACK
        # remove `vertex` from sortedOrder, put all its children back to consider
        # the next source instead of current source vertex
        sortedOrder.remove(vertex)
        for child in graph[vertex]:
            indegrees[child] += 1

    # if sortedOrder doesn't contain all tasks. Either we have cyclic dependency
    # or we have not processed all tasks in recursive call
    if len(sortedOrder) == len(indegrees):
        print(sortedOrder)


def print_orders(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return
    
    # 1. initialize indegrees and graph
    indegrees = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    # 2. build graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        indegrees[child] += 1

    # 3. find source vertices
    sources = deque()
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)

    # 4. recursively iterate over sources
    print_all_topological_sort(indegrees, graph, sources, sortedOrder)


if __name__ == "__main__":
    print('Sorted Orders')
    print_orders(3, [[0, 1], [1, 2]])
    print('Sorted Orders')
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    print('Sorted Orders')
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


'''
there can be N! combinations for ‘N’ numbers, therefore the time and space complexity of our algorithm will be O(V!∗E) where ‘V’ is the total number of tasks and ‘E’ is the total prerequisites. We need the ‘E’ part because in each recursive call, at max, we remove (and add back) all the edges.
'''