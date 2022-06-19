'''
Search in Rotated Array (medium) #

Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given 'key' is present in it.

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.
'''

def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        
        # when the numbers at indices start, middle, and end are the same, as in case 2, 
        # we can’t decide which part of the array is sorted. 
        # In such a case, the best we can do is to skip one number from both ends
        # we can skip this `if` if elements are `unique`

        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1
            end -= 1

        elif arr[start] <= arr[mid]: # left is ascending
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:                       # right is ascending (sorted)
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1


if __name__ == "__main__":
    print(search_rotated_array([10, 15, 1, 3, 8], key = 15))
    print(search_rotated_array([3, 7, 3, 3, 3], key = 7))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], key = 10))
