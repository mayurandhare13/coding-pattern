#/usr/local/bin/python3

def can_partition_helper(dp, nums, index, _sum1, _sum2):
    # base case
    if index == len(nums):
        return abs(_sum1 - _sum2)

    if dp[index][_sum1] == -1:
        # add current index num to first set
        diff1 = can_partition_helper(
            dp, nums, index + 1, _sum1 + nums[index], _sum2
        )

        # add current index num to second set
        diff2 = can_partition_helper(
            dp, nums, index + 1, _sum1, _sum2 + nums[index]
        )

        dp[index][_sum1] = min(diff1, diff2)
    
    return dp[index][_sum1]

def can_partition(nums):
    total_sum = sum(nums)
    dp = [[-1 for _ in range(total_sum + 1)] for i in range(len(nums))]
    return can_partition_helper(dp, nums, 0, 0, 0)


if __name__ == "__main__":
    print(can_partition([1, 2, 3, 9]))
    print(can_partition([1, 2, 7, 1, 5]))
    print(can_partition([1, 3, 100, 4]))
