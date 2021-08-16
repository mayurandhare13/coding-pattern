import bisect


def smallerCounts(nums: list) -> list:
    result = []
    sortedNums = []

    for num in reversed(nums):
        i = bisect.bisect_left(sortedNums, num)
        result.append(i)
        bisect.insort(sortedNums, num)
    
    return list(reversed(result))


if __name__ == '__main__':
    assert smallerCounts([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
