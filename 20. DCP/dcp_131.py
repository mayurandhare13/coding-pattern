'''
This problem has a straightforward solution using O(n) space:

1. Create a clone of the linked list, disregarding random pointers.
2. Make a hashmap that maps from an original node to its cloned counterpart.
3. Iterate through both the clone and originals at the same time. For a given clone node, find the original's random clone counterpart in the hashmap, and set it as its random node.


O(1)

1. First, double the linked list by interleaving it with cloned nodes (without random set). For example, given 1 -> 2 -> 3, becomes 1 -> 1 -> 2 -> 2 -> 3 -> 3.
2. Set the cloned nodes' random by following the original, previous node's random.next.
3. Restore the linked lists by separating them. For example, each original nodes need to set node.next = node.next.next.
'''

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def double(root: Node):
    node = root
    while node:
        copy = Node(node.val)
        next = node.next

        node.next = copy
        copy.next = next

        node = next

    return root


def setRandomPointer(node: Node):
    while node:
        node.next.random = node.random.next
        node = node.next.next


def clone(root: Node):
    root = double(root)
    setRandomPointer(root)

    node = root
    while node:
        clonedMatch = node.next
        if clonedMatch.next:
            node.next, clonedMatch.next = node.next.next, clonedMatch.next.next
        else:
            node.next, clonedMatch.next = node.next.next, None
        
        node = node.next

    return root
