cache = [0]

def _preprocess(nums: list):
    n = len(nums)
    total = 0

    for num in nums:
        total += num
        cache.append(total)


def subarraySum(nums, i, j):
    if i < 0 or j > len(nums) or i > j:
        return -1

    return cache[j] - cache[i]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    _preprocess([1, 2, 3, 4, 5])

    assert subarraySum(nums, 1, 3) == 5
    assert subarraySum(nums, 0, 5) == 15
    assert subarraySum(nums, 0, 4) == 10
    assert subarraySum(nums, 3, 4) == 4
    assert subarraySum(nums, 3, 3) == 0
