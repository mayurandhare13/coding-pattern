'''
Subset Sum (medium)

Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
'''

def can_partition_helper(nums, _sum, index):
    if _sum == 0:
        return True

    if index < 0 or index >= len(nums):
        return False
    
    if nums[index] <= _sum:
        if can_partition_helper(nums, _sum - nums[index], index + 1):
            return True
    
    return can_partition_helper(nums, _sum, index + 1)


def can_partition(nums, _sum):
    if sum(nums) < _sum:
        return False

    return can_partition_helper(nums, _sum, 0)


if __name__ == "__main__":
    print(can_partition([1, 2, 3, 7], 6))
    print(can_partition([1, 3, 4, 8], 6))
    print(can_partition([1, 2, 7, 1, 5], 10))
