from collections import deque

graph = {
    0 : [1, 3],
    1 : [2, 3],
    2 : [3],
    3 : [2, 4],
}

def recontruct_path(start, end):
    prev = bfs(start)

    path = []
    at = end
    while at != -1:
        path.append(at)
        at = prev[at]
    
    path.reverse()

    return path if path[0] == start else []


def bfs(start):
    prev = [-1] * (len(graph)+1)
    visited = [False] * (len(graph)+1)

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()

        edges = graph.get(node, None)

        if edges:
            for edge in edges:
                if not visited[edge]:
                    queue.append(edge)
                    prev[edge] = node   # set the child node index -> parent
                    visited[edge] = True

    return prev


if __name__ == "__main__":
    path = recontruct_path(0, 4)
    print(path, sep='->')