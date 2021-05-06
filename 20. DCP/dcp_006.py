from collections import defaultdict

class Node:
    def __init__(self, k, v) -> None:
        self.key = k
        self.val = v
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0
    
    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return
        
        if not node:
            node = self._sentinel.prev
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

        return node


class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        
        Three things to maintain:
        
        1. a dict, named as `self._nodes`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.
           
        2. Each frequency has a doubly linked list, store in `self._freq`, where key
           is the frequency, and value is an object of `DLinkedList`
        
        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
		   two rules:
           
           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.
           
           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)
           
        """
        self._size = 0
        self._capacity = capacity
        self._nodes = {}
        self._freq = defaultdict(DLinkedList)
        self._minfreq = 0


    def _update(self, node):
        freq = node.freq
        self._freq[freq].pop(node)

        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)


    def get(self, key):
        if key not in self._nodes:
            return -1

        node = self._nodes[key]
        self._update(node)

        return node.val

    def put(self, key, value):
        if self._capacity == 0:
            return
        
        if key in self._nodes:
            node = self._nodes[key]
            self._update(node)
            node.val = value
        else:
            if self._capacity == self._size:
                node = self._freq[self._minfreq].pop()
                print (f"deleting {node.key}")
                del self._nodes[node.key]
                self._size -= 1
            
            node = Node(key, value)
            self._nodes[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1


if __name__ == '__main__':
    c = LFUCache(2)
    c.put(1, 1)         # cache=[1,_], cnt(1)=1
    c.put(2, 2)         # cache=[2,1], cnt(2)=1, cnt(1)=1
    print(c.get(1))     # return 1
                        # cache=[1,2], cnt(1)=2, cnt(2)=1
    
    c.put(3, 3)         # 2 is the LFU key bcuz cnt(2)=1 is the smallest, invalidate 2.
    
    print(c.get(2))     # return -1 (not found)
    print(c.get(3))     # return 3
                        # cache=[3,1], cnt(3)=2, cnt(1)=2

    c.put(4, 4)         # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                        # cache=[4,3], cnt(4)=1, cnt(3)=2

    print(c.get(1))     # return -1 (not found)
    print(c.get(3))     # return 3
                        # cache=[3,4], cnt(3)=3, cnt(4)=1
    print(c.get(4))     # return 4
                        # cache=[3,4], cnt(4)=2, cnt(3)=3
