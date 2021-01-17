'''
How do we find the rotation count of a sorted and rotated array that has duplicates too?

Input: [3, 3, 7, 3]
Output: 3
Explanation: The array has been rotated 3 times
'''


def count_rotations_with_duplicates(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        
        if start < mid and arr[mid] < arr[mid - 1]:
            return mid

        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            if arr[start] > arr[start + 1]:
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:
                return end
            end -= 1

        # Left sorted, pivot is on Right
        if arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:
            end = mid - 1
    
    return 0


if __name__ == "__main__":
    print(count_rotations_with_duplicates([3, 3, 7, 3]))
