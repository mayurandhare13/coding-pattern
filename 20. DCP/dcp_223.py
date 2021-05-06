class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val} = [l={self.left}, r={self.right}]"


# Inorder traversal
# Left - Root - Right

def morrisTraversal(root):
    # set current to root of binary tree
    current = root

    while current:

        if current.left is None:
            print(current.val)
            current = current.right

        else:
            # find previous of current (Inorder)
            prev = current.left
            while prev.right is not None and prev.right != current:
                prev = prev.right

            # make current as right of its prev
            if prev.right is None:
                prev.right = current
                current = current.left
            
            # fix the right child of prev
            else:
                prev.right = None
                print(current.val)
                current = current.right


if __name__ == '__main__':
    root = Node(4) 
    root.left = Node(2) 
    root.right = Node(5) 
    root.left.left = Node(1) 
    root.left.right = Node(3) 

    morrisTraversal(root) 
