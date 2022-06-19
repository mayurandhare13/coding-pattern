import bisect

# bisect_left
def search(nums, x):
    lo, hi = 0, len(nums)
    
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    
    return lo


def smallerCounts(nums: list) -> list:
    result = []
    sortedNums = []

    for num in reversed(nums):
        i = bisect.bisect_left(sortedNums, num)
        result.append(i)
        sortedNums.insert(i, num)
    
    return list(reversed(result))


if __name__ == '__main__':
    assert smallerCounts([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
