def helper(nums: list, sum1, sum2, index):
    if index == len(nums):
        return abs(sum1 - sum2)
    
    diff1 = helper(nums, sum1 + nums[index], sum2, index + 1)
    diff2 = helper(nums, sum1, sum2 + nums[index], index + 1)

    return min(diff1, diff2)


def smallestDifference(nums: list):
    return helper(nums, 0, 0, 0)


if __name__ == '__main__':
    assert smallestDifference([5, 10, 15, 20, 25]) == 5
