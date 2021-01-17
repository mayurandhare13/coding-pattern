from collections import Counter
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxFreq = 0

        
    def push(self, x: int) -> None:
        f = self.freq[x] + 1
        self.freq[x] = f
        
        if f > self.maxFreq:
            self.maxFreq = f
            # keep track of freq --> list(elements)
        self.group[f].append(x)
            

    def pop(self) -> int:
        x = self.group[self.maxFreq].pop()
        self.freq[x] -= 1

        # reset the maxFreq value for next POP operation
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        
        return x


if __name__ == "__main__":
    obj = FreqStack()
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    
    print("max frequency: ", obj.pop())
    print("max frequency: ", obj.pop())
    print("max frequency: ", obj.pop())
    print("max frequency: ", obj.pop())
