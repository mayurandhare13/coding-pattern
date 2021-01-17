'''
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.
'''

def count_rotations(arr):
    if arr and len(arr) == 1:
        return 0

    start, end = 0, len(arr) - 1
    while arr[start] > arr[end]:
        mid = start + (end - start) // 2
        # if mid < end and arr[mid] > arr[mid + 1]:
        #     return mid + 1
        
        # if start < mid and arr[mid] < arr[mid - 1]:
        #     return mid

        if arr[mid] < arr[end]:     # right sorted, pivot on left
            end = mid
        else:                       # left sorted, pivot on right
            start = mid + 1
    
    return (start, arr[start])


if __name__ == "__main__":
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))
    print(count_rotations([5, 4, 3, 2, 1]))
