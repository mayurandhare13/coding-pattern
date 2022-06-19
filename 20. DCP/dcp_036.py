class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def insert(node, key):
     
    # If the tree is empty, return a new node
    if node == None:
        return Node(key)
 
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
 
    # return the (unchanged) node pointer
    return node


def deleteTree(node: Node):
  
    if (node == None):
        return
  
    deleteTree(node.left) 
    node.left = None
    deleteTree(node.right) 
    node.right = None


def reverseInorder(root: Node, c: list):
    if root is None or c[0] >= 2:
        return
    
    # visit largest element first
    reverseInorder(root.right, c)

    c[0] += 1

    if c[0] == 2:
        print (f"second largest: {root.key}")
        return
    
    reverseInorder(root.left, c)


def secondLargest(root: Node):
    c = [0]
    reverseInorder(root, c)


if __name__ == '__main__':

    #        50
    #     /     \
    #     30     70
    #    / \     / \
    #    20 40  60 80

    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
 
    secondLargest(root) # 70

    deleteTree(root)
    root = None

    root = Node(5)
    insert(root, 3)
    insert(root, 8)
    insert(root, 2)
    insert(root, 4)
    insert(root, 7)
    insert(root, 9)
    
    secondLargest(root) # 8
    
    deleteTree(root)
    root = None
