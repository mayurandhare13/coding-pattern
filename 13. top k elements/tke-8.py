'''
'K' Closest Numbers (medium)

Given a sorted number array and two integers 'K' and 'X', find 'K' closest numbers to 'X' in the array. Return the numbers in the sorted order. 'X' is not necessarily present in the array.

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
'''

from heapq import *


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while (low <= high):
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    # if low > 0:
    #     return low - 1
    return low


def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    low, high = index - K, index + K
    low = max(low, 0)
    high = min(high, len(arr))

    minHeap = []
    for i in range(low, high):
        heappush(minHeap, (abs(X - arr[i]), arr[i]))

    # return only K closest element
    result = []
    for _ in range(K):
        result.append(heappop(minHeap)[1])

    result.sort()
    return result


if __name__ == "__main__":
    print(find_closest_elements([5, 6, 7, 8, 9], K = 3, X = 7))
    print(find_closest_elements([2, 4, 5, 6, 9], K = 3, X = 1))
    print(find_closest_elements([2, 4, 5, 6, 9], K = 3, X = 10))
