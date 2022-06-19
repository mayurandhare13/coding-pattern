from heapq import heappush, heappop

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def __lt__(self, other):
        return self.key <= other.key


def printLL(head: Node):
    ref = head
    while ref:
        print(ref.key, end='->')
        ref = ref.next

    print('None')


def mergeLinkedList(lists: list[Node]):
    head = Node(0)
    ref = head

    minHeap = []

    for ll in lists:
        heappush(minHeap, ll)

    while minHeap:
        node = heappop(minHeap)
        ref.next = node
        ref = ref.next

        if node.next is not None:
            heappush(minHeap, node.next)

    return head.next



if __name__ == '__main__':
    h1 = Node(1)
    h1.next = Node(3)
    h1.next.next = Node(5)

    h2 = Node(2)
    h2.next = Node(3)
    h2.next.next = Node(9)

    h3 = Node(4)
    h3.next = Node(5)
    h3.next.next = Node(6)
    h3.next.next.next = Node(8)

    head = mergeLinkedList([h1, h2, h3])
    printLL(head)


# (nlogk)
# The comparison cost will be reduced to O(log k) for every pop and insertion to a priority queue. 
# But finding the node with the smallest value just costs O(1) time.
