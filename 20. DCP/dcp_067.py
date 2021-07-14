from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, k, v) -> None:
        self.key = k
        self.val = v
        self.freq = 1


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freq2nodes = defaultdict(OrderedDict)
        self._nodes = {}
        self.minfreq = 1
    

    def get(self, key):
        if key not in self._nodes:
            return -1

        node = self._nodes[key]
        del self.freq2nodes[node.freq][key]

        if not self.freq2nodes[node.freq]:
            del self.freq2nodes[node.freq]

        node.freq += 1
        self.freq2nodes[node.freq][key] = node

        if not self.freq2nodes[self.minfreq]:
            self.minfreq += 1

        return node.val


    def put(self, key, val):
        if self.capacity == 0:
            return

        if key in self._nodes:
            self._nodes[key].val = val
            self.get(key)
            return

        if len(self._nodes) == self.capacity:
            # popitem(last=False) is FIFO, like queue | LRU
            # it return key and value!!
            k, n = self.freq2nodes[self.minfreq].popitem(last=False)
            del self._nodes[k]
            if not self.freq2nodes[self.minfreq]:
                del self.freq2nodes[self.minfreq]

        node = Node(key, val)
        self.freq2nodes[1][key] = self._nodes[key] = node
        self.minfreq = 1


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