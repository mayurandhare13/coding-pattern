from collections import defaultdict

graph = defaultdict(list)
visited = set()
result = []
lows = {}


def dfs(id, prev, node):
    visited.add(node)
    lows[node] = id

    for nei in graph[node]:
        if nei == prev:
            continue

        if nei not in visited:
            dfs(id + 1, node, nei)

        lows[node] = min(lows[node], lows[nei])

        if id < lows[nei]:
            result.append([node, nei])



def criticalConnections(n: int, connections: list[list[int]]) -> list[list[int]]:
    for k, v in connections:
        graph[k].append(v)
        graph[v].append(k)
    
    dfs(0, -1, 0)
    return result


if __name__ == '__main__':
    connections = [[0,1],[1,2],[2,0],[1,3]]
    print(criticalConnections(4, connections))

