'''
Find the Smallest Missing Positive Number (medium) #
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

NOTE Ignore all numbers that are out of the range of the array (i.e., all negative numbers and all numbers greater than or equal to the length of the array)
'''

def find_first_missing_positive(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1                                         # correct index position
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return len(nums) + 1


if __name__ == "__main__":
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))
