'''
Cyclic Sort (easy)
Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. 
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
'''


def cyclic_sort(nums):
    i, n = 0, len(nums)

    while i < n:
        if nums[i] == i+1:
            i += 1
        else:               # replace current index number with right index
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    return nums

# can work with duplicates
def cyclic_sort2(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return nums


if __name__ == "__main__":
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort2([1, 4, 6, 4, 3, 2]))
