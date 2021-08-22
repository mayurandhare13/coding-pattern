'''
1. reverse the first n - k elements
2. reverse the rest of them
3. reverse the entire array
'''


def reverse(nums: list, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums: list, k):
    n = len(nums)
    k, end = k % n, n - 1

    reverse(nums, 0, end - k)
    reverse(nums, end - k + 1, end)
    reverse(nums, 0, end)


def rotateLeft(nums: list, k):
    n = len(nums)
    for i in range(n):
        print(nums[(i+k) % n] , end=' ')

    print()
    # nums[:] = nums[k:] + nums[:k]
    # print(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    rotate(nums, 2)
    assert nums == [4, 5, 1, 2, 3]

    nums2 = [1, 2, 3, 4, 5]
    rotateLeft(nums2, 2)