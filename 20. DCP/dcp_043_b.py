from heapq import heappush, heappop

class MaxStack:
    def __init__(self) -> None:
        self.softdelete = set()
        self.maxheap = []
        self.stack = []
        self.id = 0
    

    def push(self, x: int):
        self.stack.append((x, self.id))
        heappush(self.maxheap, (-x, self.id))
        self.id -= 1


    def _cleanup(self):
        while self.stack and self.stack[-1][1] in self.softdelete:
            self.softdelete.remove(self.stack.pop()[1])
        
        while self.maxheap and self.maxheap[0][1] in self.softdelete:
            self.softdelete.remove(heappop(self.maxheap)[1])


    def top(self):
        return self.stack[-1][0] if self.stack else None


    def pop(self):
        entry = self.stack.pop()
        self.softdelete.add(entry[1])
        self._cleanup()
        return entry[0]


    def max(self):
        return -self.maxheap[0][0] if self.maxheap else None


    def popmax(self):
        entry = heappop(self.maxheap)
        self.softdelete.add(entry[1])
        self._cleanup()
        return -entry[0]


if __name__ == '__main__':
    s = MaxStack()
    s.push(3)
    s.push(10)
    s.push(2)
    s.push(5)
    print (s.max()) # 10
    print(s.pop())

    print(s.pop())
    print(s.pop())
    print (s.max()) # 3
    print(s.pop())

    print(not s.max())
