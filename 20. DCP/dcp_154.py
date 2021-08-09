from heapq import heappush, heappop


# O(log n) time
# we can use counter or len(_heap)

class MaxHeap:
    def __init__(self) -> None:
        self._heap = []
        self.counter = 0
    

    def push(self, item):
        self.counter += 1
        heappush(self._heap, (-self.counter, item))
    

    def pop(self):
        _, item = heappop(self._heap)
        self.counter -= 1

        return item


class Stack:
    def __init__(self) -> None:
        self.maxHeap = MaxHeap()
    

    def push(self, item):
        self.maxHeap.push(item)


    def pop(self):
        return self.maxHeap.pop()



if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(7)
    s.push(4)
    assert s.pop() == 4
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 7
    assert s.pop() == 1
