'''
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Input: [10, 6, 4], key = 4
Output: 2
'''

def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    isAscending = arr[start] < arr[end]
    
    while start <= end:
        mid = start + (end - start) // 2    # avoid integer overflow
        if arr[mid] == key:
            return mid
        
        if isAscending:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1


if __name__ == "__main__":
    print(binary_search([4, 6, 10], key = 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], key = 5))
    print(binary_search([10, 6, 4], key = 10))
    print(binary_search([10, 6, 4], key = 4))
