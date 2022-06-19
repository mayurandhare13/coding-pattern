class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "{} => (l: {}, r: {})".format(
            self.val, self.left, self.right)


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def getMiddle(head: ListNode):
    prev = None
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    if prev:
        prev.next = None
    
    return slow


def buildTree(head: ListNode):
    if not head:
        return None
    
    mid = getMiddle(head)
    root = Tree(mid.val)

    # single node | leaf node
    if head == mid:
        return root

    root.left = buildTree(head)
    root.right = buildTree(mid.next)

    return root


# --------------------------------------

def size(head: ListNode):
    count = 0
    ptr = head
    while ptr:
        count += 1
        ptr = ptr.next
    
    return count


def buildTree2(head: ListNode):
    total = size(head)

    def helper(l, r):
        nonlocal head
        if l > r:
            return None

        mid = l + (r - l) // 2
        left = helper(l, mid - 1)
        
        root = Tree(head.val)
        root.left = left

        # LL is sorted. We traverse inorder binary search tree
        head = head.next

        root.right = helper(mid + 1, r)

        return root
    
    return helper(0, total - 1)



if __name__ == '__main__':
    head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))

    root = buildTree(head)
    print(root)

    assert root.left.val == -3
    assert root.right.left.val == 5

    root = buildTree2(head)
    print(root)
