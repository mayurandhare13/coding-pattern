'''
[1, 2, 3, 4, 5, 6] and k = 2.

reverse from 0 to k: [2, 1, 3, 4, 5, 6]
reverse from k to n: [2, 1, 6, 5, 4, 3]
reverse from 0 to n: [3, 4, 5, 6, 1, 2]
'''

# reversing a list takes O(n)
def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


def rotate(nums: list, k):
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums) - 1)
    reverse(nums, 0, len(nums) - 1)

    return nums


if __name__ == '__main__':
    assert rotate([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
