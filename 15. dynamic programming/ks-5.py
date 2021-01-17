'''
Count of Subset Sum (hard) #
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
'''

def count_subsets_helper(nums, _sum, index):
    # base case
    if _sum == 0:
        return 1
    
    if len(nums) == 0 or index >= len(nums):
        return 0
        
    _sum1 = 0
    if nums[index] <= _sum:
        _sum1 = count_subsets_helper(
            nums, _sum - nums[index], index + 1
        )
    
    _sum2 = count_subsets_helper(nums, _sum, index + 1)

    return _sum1 + _sum2

def count_subsets(nums, sum):
    return count_subsets_helper(nums, sum, 0)


if __name__ == "__main__":
    print(count_subsets([1, 1, 2, 3], 4))
    print(count_subsets([1, 2, 7, 1, 5], 9))
