'''
Given an array of numbers sorted in ascending order, find the range of a given number 'key'. The range of the 'key' will be the first and last position of the 'key' in the array.

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
'''

def find_range(arr, key):
    result = [-1, -1]
    
    # search min index
    result[0] = binary_search(arr, key, False)

    # search max index
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)

    return result


def binary_search(arr, key, findMaxIndex):
    keyIndex = -1
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            keyIndex = mid
            if findMaxIndex:
                start = mid + 1
            else:
                end = mid - 1

    return keyIndex


if __name__ == "__main__":
    print(find_range([4, 6, 6, 6, 9], key = 6))
    print(find_range([1, 3, 8, 10, 15], key = 10))
    print(find_range([1, 3, 8, 10, 15], key = 12))