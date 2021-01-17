'''
Minimum Subset Sum Difference (hard)

Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
'''

def can_partition_helper(nums, index, _sum1, _sum2):
    # base case
    if index == len(nums):
        return abs(_sum1 - _sum2)

    # add current index num to first set
    diff1 = can_partition_helper(
        nums, index + 1, _sum1 + nums[index], _sum2
    )

    # add current index num to second set
    diff2 = can_partition_helper(
        nums, index + 1, _sum1, _sum2 + nums[index]
    )

    return min(diff1, diff2)


def can_partition(nums):
    return can_partition_helper(nums, 0, 0, 0)


if __name__ == "__main__":
    print(can_partition([1, 2, 3, 9]))
    print(can_partition([1, 2, 7, 1, 5]))
    print(can_partition([1, 3, 100, 4]))
