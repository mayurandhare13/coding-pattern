def can_partition_handler(dp, nums, _sum, index):
    # base case
    if _sum == 0:
        return 1

    if index < 0 or index >= len(nums):
        return 0
    
    if dp[index][_sum] == -1:
        # if number at `current index` > sum, then we don't process this element
        if nums[index] <= _sum:
            if can_partition_handler(dp, nums, _sum - nums[index], index + 1) == 1:
                dp[index][_sum] = 1
                return 1
        
        dp[index][_sum] = can_partition_handler(dp, nums, _sum, index + 1)

    return dp[index][_sum]


def can_partition(nums):
    nums_sum = sum(nums)
    if nums_sum % 2 != 0:
        return False
    
    # init dp array, -1 default, 1 true, 0 false
    dp = [[ -1 for _ in range(int(nums_sum / 2) + 1)] for i in range(len(nums))]

    return True if can_partition_handler(dp, nums, nums_sum // 2, 0) == 1 else False


if __name__ == "__main__":
    print(can_partition([1, 2, 3, 4]))
    print(can_partition([1, 1, 3, 4, 7]))
    print(can_partition([2, 3, 4, 6]))
