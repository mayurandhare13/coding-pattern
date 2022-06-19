class Stack:
    def __init__(self):
        self.stack = []
        # we can also keep only max-value `index` (length of stack) in maxStack
        # then when val from stack gets pop then only index 
        # if len(self.stack) - 1 == self.max_stack[-1]:
        #     self.max_stack.pop()

        self.maxStack = []

    def push(self, val):
        self.stack.append(val)
        
        if not self.maxStack or val > self.maxStack[-1]:
            self.maxStack.append(val)
    
    def pop(self):
        if not self.stack:
            return None
        
        returnVal = self.stack.pop()
        if returnVal == self.maxStack[-1]:
            self.maxStack.pop()
        
        return returnVal


    def max(self):
        if not self.maxStack:
            return None
        
        return self.maxStack[-1]


    def popMax(self):
        """
        :rtype: int
        """
        maxElement = self.max()
        maxIndex = 0
        for i in range(len(self.stack) - 1, -1, -1):
            if maxElement == self.stack[i]:
                maxIndex = i
                break
        return self.stack.pop(maxIndex)


if __name__ == '__main__':
    s = Stack()
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

