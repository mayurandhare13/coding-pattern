'''
Merge K Sorted Lists

Given an array of 'K' sorted LinkedLists, merge them into one sorted list.
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
'''

from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    # used for min heap
    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    minHeap = []

    # put root of all lists in min heap
    for lst in lists:
        if lst is not None:
            heappush(minHeap, lst)

    resultHead, resultTail = None, None
    while minHeap:
        node = heappop(minHeap)
        if resultHead is None:
            resultHead = resultTail = node
        else:
            resultTail.next = node
            resultTail = resultTail.next
        
        if node.next is not None:
            heappush(minHeap, node.next)
    
    return resultHead



if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Merged List")
    while result is not None:
        print(str(result.value), sep=' ', end=' ')
        result =result.next
    
    l4 = ListNode(5)
    l4.next = ListNode(8)
    l4.next.next = ListNode(9)

    l5 = ListNode(1)
    l5.next = ListNode(7)

    result2 = merge_lists([l4, l5])
    print("\nMerged List")
    while result2 is not None:
        print(str(result2.value), sep=' ', end=' ')
        result2 =result2.next
