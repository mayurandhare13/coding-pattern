'''
Rotate a LinkedList (medium) #
Given the head of a Singly LinkedList and a number 'k', rotate the LinkedList to the right by 'k' nodes.
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, rotations):
    if head is None or head.next is None or rotations <= 0:
        return head
    
    # find the length and the last node of the list
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    # connect the last node with the head to make it a circular list
    last_node.next = head

    # no need to do rotations more than the length of the list | corner case
    rotations %= list_length

    skip_length = list_length - rotations - 1
    last_node_of_rotated_list = head
    while skip_length > 0:
        last_node_of_rotated_list = last_node_of_rotated_list.next
        skip_length -= 1

    # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    rotations = 4
    
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    print("rotations: ", rotations)
    result = rotate(head, rotations)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()
