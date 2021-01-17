'''
Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Input: 1->1->1->2->3
Output: 2->3
'''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.val) + " ", end='')
            temp = temp.next
        print()

def deleteDuplicates(head):
    dummy_node = Node(0)
    dummy_node.next = head

    slow = dummy_node
    fast = head

    while fast is not None:
        duplicate = False

        while fast.next is not None and fast.val == fast.next.val:
            duplicate = True
            fast = fast.next
        
        # if no duplicates
        if not duplicate:
            slow = slow.next
            
        # duplicate / no-duplicate, connect to next node.
        # even if next node is duplicate then also it will override in next iteration
        slow.next = fast.next
        fast = fast.next

    return dummy_node.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(5)

    new_head = deleteDuplicates(head)
    new_head.print_list()
