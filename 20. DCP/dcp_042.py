# refer dcp_034_b.py

def subsetSumHelper(nums: list, idx, k):
    if idx >= len(nums):
        return None
    
    if nums[idx] == k:
        return [nums[idx]]

    withInclude = subsetSumHelper(nums, idx + 1, k - nums[idx])
    if withInclude:
        return [nums[idx]] + withInclude
    
    return subsetSumHelper(nums, idx + 1, k)


def subsetSum(nums: list, k):
    return subsetSumHelper(nums, 0, k)


if __name__ == '__main__':
    assert subsetSum([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
    assert subsetSum([12, 1, 61, 5, -108, 2], -106) == [-108, 2]
