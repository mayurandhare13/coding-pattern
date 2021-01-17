
def count_subsets_helper(nums, _sum, index, dp):
    # base case
    if _sum == 0:
        return 1
    
    if len(nums) == 0 or index >= len(nums):
        return 0
    
    if dp[index][_sum] == -1:
        _sum1 = 0
        if nums[index] <= _sum:
            _sum1 = count_subsets_helper(
                nums, _sum - nums[index], index + 1, dp
            )
        
        _sum2 = count_subsets_helper(nums, _sum, index + 1, dp)

        dp[index][_sum] = _sum1 + _sum2
    
    return dp[index][_sum]


def count_subsets(nums, sum):
    dp = [[-1 for _ in range(sum+1)] for i in range(len(nums))]
    return count_subsets_helper(nums, sum, 0, dp)


if __name__ == "__main__":
    print(count_subsets([1, 1, 2, 3], 4))
    print(count_subsets([1, 2, 7, 1, 5], 9))
