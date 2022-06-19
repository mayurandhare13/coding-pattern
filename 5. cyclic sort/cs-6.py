'''
Find all Duplicate Numbers (easy)

We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array has some duplicates, find all the duplicate numbers without using any extra space.

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
'''


def find_all_duplicates(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1             # index to swap
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    duplicateNumbers = []
    
    for i in range(len(nums)):
        if nums[i] != i + 1:
            # print (i + 1)         missing number
            duplicateNumbers.append(nums[i])

    return duplicateNumbers


def find_all_duplicates2(nums):
    i = 0
    duplicateNumbers = []

    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1             # index to swap
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                duplicateNumbers.append(nums[i])
                i += 1
        else:
            i += 1

    
    return duplicateNumbers


if __name__ == "__main__":
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates2([5, 4, 7, 2, 3, 5, 3]))
