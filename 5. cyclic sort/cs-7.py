'''
Find the Corrupt Pair (easy) #
We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array originally contained all the numbers from 1 to 'n', but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
'''


def find_corrupt_numbers(nums):
    i = 0
    currupt_pair = []
    
    # sort array
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            currupt_pair.append(nums[i])    # duplicate
            currupt_pair.append(i + 1)      # missing
            break

    return currupt_pair


if __name__ == "__main__":
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))
