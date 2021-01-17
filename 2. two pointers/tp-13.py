'''
Minimum Window Sort (medium)
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
'''

import math

def shortest_window_sort(arr):
    low, high = 0, len(arr)-1
    # find the first number out of sorting order from the beginning
    while (low < high and arr[low] < arr[low+1]):
        low += 1
        
    if (low == len(arr)-1): # already sorted
        return 0

    while (high > low and arr[high] > arr[high-1]):
        high -= 1
    
    # find the maximum and minimum of the subarray
    subarr_max = -math.inf
    subarr_min = math.inf
    for i in range(low, high+1):
        subarr_max = max(subarr_max, arr[i])
        subarr_min = min(subarr_min, arr[i])
    
    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while (low > 0 and arr[low-1] > subarr_min):
        low -= 1
    
    # extend the subarray to include any number which is lesser than the maximum of the subarray
    while (high < len(arr)-1 and arr[high+1] < subarr_max):
        high += 1
    
    return high - low + 1



if __name__ == "__main__":
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
