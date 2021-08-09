class Stack:
    def __init__(self, size) -> None:
        self.size = size
        self.list = [None] * size
        self.s0 = 0                      # grow up
        self.s1 = len(self.list) // 3    # grow up
        self.s2 = len(self.list) - 1     # grow down


    def __isResizeNeeded(self):
        return self.s0 == len(self.list) // 3 or self.s1 > self.s2

    def __resize(self, size):
        prevList = self.list
        prevS0 = self.s0
        prevS1 = self.s1
        prevS2 = self.s2

        self.list = [None] * size
        self.s0 = 0
        self.s1 = len(self.list) // 3
        self.s2 = len(self.list) - 1

        for i in range(prevS0):
            self.push(0, prevList[i])
        
        for i in range(len(prevList) // 3, prevS1):
            self.push(1, prevList[i])
        
        for i in reversed(range(prevS2 + 1, len(prevList))):
            self.push(2, prevList[i])


    def push(self, stackNumber, item):
        if stackNumber == 0:
            self.list[self.s0] = item
            self.s0 += 1

        elif stackNumber == 1:
            self.list[self.s1] = item
            self.s1 += 1

        else:
            self.list[self.s2] = item
            self.s2 -= 1

        if self.__isResizeNeeded():
            self.__resize(self.size * 2)


    def pop(self, stackNumber):
        out = 0
        if stackNumber == 0:
            self.s0 -= 1
            out = self.list[self.s0]

        elif stackNumber == 1:
            self.s1 -= 1
            out = self.list[self.s1]

        else:
            self.s2 += 1
            out = self.list[self.s2]

        return out

    def __repr__(self) -> str:
        return f"{self.list}"


if __name__ == '__main__':
    stack = Stack(10)
    stack.push(0, 0)
    stack.push(1, 3)
    stack.push(2, 6)

    stack.push(0, 1)
    stack.push(1, 4)
    stack.push(2, 7)

    stack.push(0, 2)
    stack.push(1, 5)
    stack.push(2, 8)

    stack.push(1, 9)

    print(stack)
