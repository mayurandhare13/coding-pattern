# cs-4 recursive approach

# O(n^2)
def longestSubsequence(nums: list):
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] <= nums[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


if __name__ == '__main__':
    assert longestSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
