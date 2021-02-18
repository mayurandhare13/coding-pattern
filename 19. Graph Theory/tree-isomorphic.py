from collections import deque

class TreeNode:
    
    def __init__(self, id, parent = None):
        self.id = id
        self.parent = parent
        self.children = []
    
    def addChildren(self, *nodes):
        for node in nodes:
            self.children.append(node)
        

def find_tree_centers(graph):
    n = len(graph)

    # 1. initialize `indegrees` and `undirected graph`
    indegrees = {i:0 for i in graph}

    # 2. build graph
    for node in graph:
        indegrees[node] = len(graph[node])

    # 3. find leaves with single edge
    leaves = deque()
    for key, val in indegrees.items():
        if val == 1:
            leaves.append(key)
    
    # 4. remove leaves level by level
    total_nodes = n
    while total_nodes > 2:
        leaves_size = len(leaves)
        total_nodes -= leaves_size

        for i in range(leaves_size):
            leaf = leaves.popleft()
            
            for child in graph[leaf]:
                indegrees[child] -= 1
                if indegrees[child] == 1:
                    leaves.append(child)
    
    return list(leaves)


def build_tree(graph: dict, node: TreeNode):

    for neighbor in graph.get(node.id, []):
        # ignore edge pointing back to parent
        if node.parent and neighbor == node.parent.id:
            continue
        
        child = TreeNode(neighbor, parent=node)
        node.addChildren(child)

        build_tree(graph, child)

    return node


def rootTree(graph, root_node):
    root = TreeNode(root_node)
    return build_tree(graph, root)


def encode(node: TreeNode):
    if not node:
        return ''
    
    labels = []
    for child in node.children:
        labels.append(encode(child))
    
    labels.sort()
    label_encoded = ''.join(labels)

    return '(' + label_encoded + ')'


def isIsomorphic(tree1, tree2):
    if tree1 is None or tree2 is None:
        return False
    
    centers1 = find_tree_centers(tree1)
    centers_2 = find_tree_centers(tree2)

    rootedTree1 = rootTree(tree1, centers1[0])
    tree1Encoded = encode(rootedTree1)
    print(f"tree1: {tree1Encoded}")

    for center in centers_2:
        rootedTree2 = rootTree(tree2, center)
        tree2Encoded = encode(rootedTree2)

        if tree1Encoded == tree2Encoded:
            return True

    return False


if __name__ == '__main__':
    tree1 = {2 : [0, 1, 3], 3: [4]}
    tree2 = {1 : [0, 2, 3], 2 : [4]}

    if isIsomorphic(tree1, tree2):
       print("\u2713 trees are isomorphic !!")
    else:
        print("\u274c trees are not isomorphic !!")

    tree3 = {0 : [1, 2, 3], 2 : [6, 7], 1 : [4, 5], 3 : [8], 5 : [9]}
    rootedTree3 = rootTree(tree3, 0)
    print(encode(rootedTree3))
