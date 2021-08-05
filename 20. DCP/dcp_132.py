import bisect
import math

class HitCounter:
    def __init__(self) -> None:
        self.hits = []
    
    # O(log n)    
    def record(self, timestamp):
        # timestamp is unordered
        bisect.insort_left(self.hits, timestamp)
    
    def total(self):
        return len(self.hits)

    # O(log n)    
    def range(self, lower, upper):
        left = bisect.bisect_left(self.hits, lower)
        right = bisect.bisect_right(self.hits, upper)

        return right - left


# trade-off would be to sacrifice accuracy for memory by grouping together
# timestamps in a coarser granularity, such as minute or even hours.

class HitCounter2:
    def __init__(self):
        self.counter = 0
        self.hits = []  # (timestamp in minutes, # of times)

    # O(log n)    
    def record(self, timestamp):
        self.counter += 1
        minutes = math.floor(timestamp / 60)

        i = bisect.bisect_left([hit[0] for hit in self.hits], minutes)
        
        if i < len(self.hits) and self.hits[i][0] == minutes:
            self.hits[i] = (minutes, self.hits[i][1] + 1)
        else:
            self.hits.insert(i, (minutes, 1))

    
    def total(self):
        return self.counter

    # O(log n)    
    def range(self, lower, upper):
        lowerLimit = math.floor(lower / 60)
        upperLimit = math.floor(upper / 60)

        left = bisect.bisect_left([hit[0] for hit in self.hits], lowerLimit)
        right = bisect.bisect_right([hit[0] for hit in self.hits], upperLimit)

        return sum(self.hits[i][1] for i in range(left, right))

