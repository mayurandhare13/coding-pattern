'''
Frequency Stack (hard)

Design a class that simulates a Stack data structure, implementing the following two operations:
push(int num): Pushes the number 'num' on the stack.
pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2
'''

from heapq import *

class Element:

    def __init__(self, number, frequency, sequenceNumber):
        self.number = number
        self.frequency = frequency
        self.sequenceNumber = sequenceNumber
    
    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        
        return self.sequenceNumber > other.sequenceNumber


class FrequencyStack:
    sequenceNumber = 0
    maxHeap = []
    frequencyMap = {}

    def push(self, num):
        self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
        heappush(self.maxHeap, 
                Element(num, self.frequencyMap[num], self.sequenceNumber)
        )
        self.sequenceNumber += 1
    
    def pop(self):
        num = heappop(self.maxHeap).number
        # decrement the frequency | remove it if this is last number
        if self.frequencyMap[num] > 1:
            self.frequencyMap[num] -= 1
        else:
            del self.frequencyMap[num]
        
        return num


if __name__ == "__main__":
    stack = FrequencyStack()
    stack.push(1)    
    stack.push(2)    
    stack.push(3)    
    stack.push(2)    
    stack.push(1)    
    stack.push(2)    
    stack.push(5)

    print(stack.pop())    
    print(stack.pop())    
    print(stack.pop())    
