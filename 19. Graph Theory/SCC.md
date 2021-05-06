## Strongly Connected Components

### Overview

- Can be thought of as `self contained cycle` within directed graph where every vertex in a given cycle can reach every other vertex in the same cycle

- `low-link value` of a node is the smallest _lowest_ node id reachable from that node when doing DFS (including itself)

- Depending on where DFS starts, and the order in which nodes/edges visited, the low-link values for identifying SCCs could be _wrong_

- In Targan's SCC, maintain a stack (set) of valid nodes from which to update the low-link values from

- Nodes are added to the stack (set) of valid nodes as they are explored for the first time

- Nodes are removed from the stack (set) each time a complete SCC is found

- To update the node `u`'s low-link value to node `v`'s low-link value there has to be a path of edges from `u` to `v` and node `v` must be on the stack (set)


### Algorithm

1. Mark the `id` of each node as unvisited

2. Start DFS. Upon visiting a node assign it an `id` and `low-link` value

3. Mark the current node as visited and add them to `seen stack (set)`. This is valid set of nodes to update the low-link value.

4. On DFS callback [note-1](####-note-1), if previous node is on the `seen stack` then 
    ```
    low_link[at] = min(low_link[at], low_link[to])
    ```

5. After visiting all neighbors, if the current node started a connected component [note-2](####-Note-2) then pop the nodes off stack until current node is reached.

#### Note-1 
This allows low-link values to propagate thoughout cycles  

#### Note-2 
A node started a connected component if `id[at] == low_link[at]`

[Tarjan's SCC](gt-scc.py)

