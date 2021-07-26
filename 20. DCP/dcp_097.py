from collections import defaultdict
import bisect

# python standard library doesn't have sorted map.
'''
{
    key: {
        time: value,
        time: value,
        ...
    },
    key: {
        time: value,
        time: value,
        ...
    },
    ...
}
'''


class TimeMap:
    def __init__(self) -> None:
        self.keys = []
        self.values = []

    def get(self, k):
        if self.keys is None:
            return None
        
        i = bisect.bisect_left(self.keys, k)
        if i == len(self.keys):
            return self.values[i - 1]
        
        elif self.keys[i] == k:
            return self.values[i]
        
        elif i == 0:
            return None
        
        else:
            return self.values[i - 1]

    # k: time   v: value
    def set(self, k, v):
        i = bisect.bisect_left(self.keys, k)
        if i == len(self.keys):
            self.keys.append(k)
            self.values.append(v)

        elif self.keys[i] == k:
            self.values[i] = v

        else:
            self.keys.insert(i + 1, k)
            self.values.insert(i + 1, v)



class MultiMapTime:
    def __init__(self) -> None:
        self.map = defaultdict(TimeMap)
    

    def get(self, key, time):
        timeMap = self.map.get(key)
        if timeMap is None:
            return None

        return timeMap.get(time)

    def set(self, key, value, time):
        self.map[key].set(time, value)



if __name__ == '__main__':
    d = MultiMapTime()
    d.set(1, 1, 0)              # set key 1 to value 1 at time 0
    d.set(1, 2, 2)              # set key 1 to value 2 at time 2
    assert d.get(1, 1) == 1     # get key 1 at time 1 should be 1
    assert d.get(1, 3) == 2     # get key 1 at time 3 should be 2
    d.set(1, 1, 5)              # set key 1 to value 1 at time 5
    assert d.get(1, 0) == 1     # get key 1 at time 0 should be 1
    assert d.get(1, 10) == 1    # get key 1 at time 10 should be 1
    d.set(1, 1, 0)              # set key 1 to value 1 at time 0
    d.set(1, 2, 0)              # set key 1 to value 2 at time 0
    assert d.get(1, 0) == 2     # get key 1 at time 0 should be 2
