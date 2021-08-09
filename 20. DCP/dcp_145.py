# recursive solution refer ll-3.py
class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next


def swapNodes(root: Node):
    curr = root

    while curr and curr.next:
        curr.val, curr.next.val = curr.next.val, curr.val
        curr = curr.next.next
    
    return root



def swapNodes2(head: Node):
    if not head or not head.next:
        return head
    
    # nodes to be swapped
    first = head
    second = head.next

    first.next = swapNodes2(second.next)
    second.next = first

    # now head is the second node
    return second


def swapPairs(head: Node):
    dummy = Node(-1)
    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        prev.next = second

        first.next = second.next
        second.next = first

        # reinitialize prev and head node
        prev = first
        head = first.next

    return dummy.next


if __name__ == '__main__':
    root = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    curr = swapNodes2(root)
    
    while curr:
        print(curr.val, end=' -> ')
        curr = curr.next
    
    print('None')
