'''
Search Bitonic Array (medium)

Given a Bitonic array, find if a given ‘key’ is present in it. 

Input: [1, 3, 8, 4, 3], key=4
Output: 3
'''

def search_bitonic_array(arr, key):
    maxIndex = find_max_in_bitonic_array(arr)
    keyIndex = binary_search(arr, key, 0, maxIndex)
    if keyIndex != -1:
        return keyIndex
    return binary_search(arr, key, maxIndex + 1, len(arr) - 1)


def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    
    while start < end:
        mid = start + (end - start) // 2
        
        # second half is descending
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    
    return start


def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        
        if arr[start] <= arr[end]:
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
    print(search_bitonic_array([1, 3, 8, 4, 3], key=4))
    print(search_bitonic_array([3, 8, 3, 1], key=8))
    print(search_bitonic_array([1, 3, 8, 12], key=12))
    print(search_bitonic_array([10, 9, 8], key=10))
