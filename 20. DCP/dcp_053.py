class MyQueue:
    def __init__(self) -> None:
        self.main = []
        self.aux = []


    def enqueue(self, x: int):
        self.main.append(x)
    

    def dequeue(self):
        if not self.aux:
            while self.main:
                self.aux.append(self.main.pop())
        
        return self.aux.pop()


if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
