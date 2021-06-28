class Order:
    def __init__(self, N):
        self.logs = list()
        self.N = N
    
    def __repr__(self):
        return str(self.logs)

    def record(self, recordId: int):
        if len(self.logs) == self.N:
            self.logs.pop(0)
        
        self.logs.append(recordId)
    
    def getLast(self, i: int):
        return self.logs[-i]


if __name__ == '__main__':
    log = Order(5)
    log.record(1)
    log.record(2)
    print(log)      # [1, 2]
    
    log.record(3)
    log.record(4)
    log.record(5)
    print(log)      # [1, 2, 3, 4, 5]

    log.record(6)
    log.record(7)
    log.record(8)
    print(log)      # [4, 5, 6, 7, 8]

    assert log.getLast(4) == 5
    assert log.getLast(1) == 8
        