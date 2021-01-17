'''
Equal Subset Sum Partition (medium)
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
'''

def can_partition_handler(nums, _sum, index):
    # base case
    if _sum == 0:
        return True

    if index < 0 or index >= len(nums):
        return False

    # if number at `current index` > sum, then we don't process this element
    if nums[index] <= _sum:
        if can_partition_handler(nums, _sum - nums[index], index + 1):
            return True
    
    return can_partition_handler(nums, _sum, index + 1)


def can_partition(nums):
    nums_sum = sum(nums)
    if nums_sum % 2 != 0:
        return False
    
    return can_partition_handler(nums, nums_sum // 2, 0)


if __name__ == "__main__":
    print(can_partition([1, 2, 3, 4]))
    print(can_partition([1, 1, 3, 4, 7]))
    print(can_partition([2, 3, 4, 6]))
