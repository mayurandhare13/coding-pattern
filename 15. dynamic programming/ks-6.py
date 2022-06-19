'''
Target Sum (hard) #
You are given a set of positive numbers and a target sum 'S'. Each number should be assigned either a '+' or '-' sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target 'S'.

Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

{+1-1-2+3}
(1 + 3) - (1 + 2 ) = 1
Sum(s1) - Sum(s2) = S           ...1
Sum(s1) + Sum(s2) = Sum(num)    ...2
Sum(s1) = (S + Sum(num)) / 2    ...1+2
'''

def find_target_subset_helper(nums, _sum, index):
    if _sum == 0:
        return 1
    
    if len(nums) <= 0 or index >= len(nums):
        return 0

    _sum1 = 0
    if nums[index] <= _sum:
        _sum1 = find_target_subset_helper(
            nums, _sum - nums[index], index + 1)
    
    _sum2 = find_target_subset_helper(nums, _sum, index + 1)

    return _sum1 + _sum2


def find_target_subset(nums, s):
    total_sum = sum(nums)
    if total_sum < s or (s + total_sum) % 2 == 1:
        return 0
    
    return find_target_subset_helper(nums, (s + total_sum) // 2, 0)


if __name__ == "__main__":
    print(find_target_subset([1, 1, 2, 3], 1))
    print(find_target_subset([1, 2, 7, 1], 9))
    print(find_target_subset([1, 0], 1))
