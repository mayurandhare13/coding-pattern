'''
Find the First K Missing Positive Numbers (hard) #
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
'''


def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)
    
    # sort the numbers except which are not in range
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
        if len(missingNumbers) < k and nums[i] != i + 1:
            missingNumbers.append(i + 1)                # missing positive number
            extraNumbers.add(nums[i])                   # duplicate & OOB
    
    # add remaining numbers
    i = 1
    while len(missingNumbers) < k:
        nextNumber = i + n
        if nextNumber not in extraNumbers:
            missingNumbers.append(nextNumber)
        i += 1
    
    return missingNumbers


if __name__ == "__main__":
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))
