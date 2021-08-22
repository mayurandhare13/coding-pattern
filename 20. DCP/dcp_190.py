# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass

def maxSubarraySum(nums: list):
    total, curMax, maxSum, curMin, minSum = 0, 0, 0, 0, 0

    for num in nums:
        curMax = max(curMax + num, num)
        maxSum = max(maxSum, curMax)

         # idea is to subtract as much negative value from total sum as possible
         # so that the result is maximum
        curMin = min(minSum + num, num)
        minSum = min(minSum, curMin)

        total += num

    return max(maxSum, total - minSum) if maxSum > 0 else maxSum


if __name__ == '__main__':
    assert maxSubarraySum([8, -1, 3, 4]) == 15
    assert maxSubarraySum([-4, 5, 1, 0]) == 6
