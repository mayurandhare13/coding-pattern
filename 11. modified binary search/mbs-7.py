'''
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.
'''

'''
moving start & end to max value | eventually start & end points to max value
If arr[mid] > arr[mid + 1], we are in the second (descending) part of the bitonic array. Therefore, our required number could either be pointed out by middle or will be before middle. This means we will be doing: end = middle.
'''


def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:     # descending part
            end = mid
        else:                           # ascending part
            start = mid + 1

    return arr[start]                   # when start == end


if __name__ == "__main__":
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))
