class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.map = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def _add(self, node):
        prevNode = self.tail.prev
        prevNode.next = node
        node.next = self.tail
        node.prev = prevNode
        self.tail.prev = node


    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


    def get(self, key):
        node = self.map.get(key, None)

        if not node:
            return -1
        
        self._remove(node)
        self._add(node)

        return node.val
    

    def set(self, key, val):
        node = self.map.get(key)
        if not node:
            node = Node(key, val)
            self._add(node)
            self.map[key] = node

            if len(self.map) > self.capacity:
                nodeToRemove = self.head.next
                del self.map[nodeToRemove.key]
                self._remove(nodeToRemove)
        else:
            node.val = val
            self._remove(node)
            self._add(node)



if __name__ == '__main__':
    lru = LRUCache(capacity=3)

    assert lru.get('a') == -1
    lru.set('a', 1)
    assert lru.get('a') == 1
    lru.set('b', 2)
    lru.set('c', 3)
    lru.set('b', 20)
    assert lru.get('b') == 20
    lru.set('d', 4)
    lru.set('e', 5)
    lru.set('a', 1)
    assert lru.get('a') == 1
    assert lru.get('b') == -1
    assert lru.get('e') == 5
    assert lru.get('c') == -1
