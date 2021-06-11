'''
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
'''

def remove_duplicates(arr):
  # index of the next non-duplicate element
    left, right = 1, 1
    while right < len(arr):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
        right += 1

    return left


def removeDuplicates(nums: list):
    n = len(nums)
    if n <= 1:
        return n

    # index to store next unique element
    # we are replacing only last element of duplicates
    j = 0
    for i in range(0, n-1):
        if nums[i] != nums[i+1]:
            nums[j] = nums[i]
            j += 1

    nums[j] = nums[n-1]
    j += 1

    return j


if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
    print(removeDuplicates([2, 2, 2, 11]))
