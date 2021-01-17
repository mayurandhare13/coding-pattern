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


if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
