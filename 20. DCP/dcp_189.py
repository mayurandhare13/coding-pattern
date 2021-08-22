from collections import defaultdict

def longestSubarray(nums: list):
    indexMap = defaultdict(int)
    start = 0
    long = 0

    for i, val in enumerate(nums):
        if val in indexMap:
            start = max(start, indexMap[val] + 1)

        indexMap[val] = i
        long = max(long, i - start + 1)
    
    return long


if __name__ == '__main__':
    assert longestSubarray([5, 1, 3, 5, 2, 3, 4, 1]) == 5
    assert longestSubarray([5, 1, 3, 5, 2, 3, 4]) == 4
