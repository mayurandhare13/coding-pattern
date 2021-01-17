graph = {
    0 : [1, 2],
    1 : [2, 3],
    2 : [2, 3],
}

visited = [False for _ in range(len(graph)+1)]

def dfs_recursive(at):
    if visited[at]:
        return 0
    
    visited[at] = True
    count = 1
    
    edges = graph.get(at, None)
    if edges:
        for edge in edges:
            count += dfs_recursive(edge)
    
    return count


node_count = dfs_recursive(0)
print("Node count starting from node 0: ", node_count)
