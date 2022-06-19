'''
Given an array of numbers sorted in an ascending order, find the ceiling of a given number 'key'. The ceiling of the 'key' will be the smallest element in the given array greater than or equal to the 'key'.

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
'''

def search_ceiling_of_number(arr, key):
    start, end = 0, len(arr) - 1
    if key > arr[end]:
        return -1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # loop will iterate till start <= end, at the end of loop, (start == end + 1) which mean we are unable to find element
    # next big element would be arr[start]
    # eg above. {mid, start, end == 15} | arr[mid] > key --> end = mid - 1
    # start is still within arr boundry, it just end < start 
    return start


if __name__ == "__main__":
    print(search_ceiling_of_number([1, 3, 8, 10, 15], key = 12))
    print(search_ceiling_of_number([4, 6, 10], key = -1))
    print(search_ceiling_of_number([4, 6, 10], key = 17))
