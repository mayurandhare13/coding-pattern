# https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0

# O(n^2)
def inversionBasic(nums: list) -> int:
    count = 0
    size = len(nums)
    for i in range(size-1):
        for j in range(i+1, size):
            if nums[i] > nums[j]:
                count += 1
    
    return count


def inversionOptimized(nums: list):
    c, count = inversionMergeSort(nums)
    return count

'''
a = [ 1, 3, 5 ]
b = [ 2, 4, 6 ]
---
c = [1] and i = 1, j = 0 then a[i] > a[j] but `a` comes before `b` in merge sort
that means 3 & 5 are greater than 2
so, total inversions = len(a) - i == 3-1 = 2 (when i is at 1)
and so on...
'''

def inversionMergeSort(nums: list):
    if len(nums) == 1:
        return nums, 0
    
    mid = len(nums) // 2

    a, ai = inversionMergeSort(nums[:mid])
    b, bi = inversionMergeSort(nums[mid:])

    c= []
    i, j = 0, 0
    inversions = ai + bi

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1

        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)

    c += a[i:]
    c += b[j:]

    return c, inversions


if __name__ == '__main__':
    assert inversionBasic([2, 4, 1, 3, 5]) == 3
    assert inversionBasic([5, 4, 3, 2, 1]) == 10

    assert inversionOptimized([2, 4, 1, 3, 5]) == 3
    assert inversionOptimized([5, 4, 3, 2, 1]) == 10
