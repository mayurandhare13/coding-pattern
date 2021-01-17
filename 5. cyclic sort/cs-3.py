'''
Find all Missing Numbers (easy)

We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
'''


def find_missing_numbers(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    missingNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers


if __name__ == "__main__":
    print(find_missing_numbers([2, 4, 1, 2])) # after sorting [1, 2, 2, 4]
    print(find_missing_numbers([2, 3, 2, 1]))
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))



'''
j = nums[i] - 1
nums[i] != nums[j]
    swap
with this way until value of nums[i] - 1 == i 
or both the values are same (duplicate)

if nums[0] = 1
nums[i] = nums[0]     {1}
nums[j] = nums[0] - 1 {1 - 1}
--> nums[j] = nums[i] - 1 
    nums[i] == nums[j]

[1, 5, 4, 3]
nums[0] = 1
nums[nums[0] - 1] = nums[0]
'''