'''
Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.
'''

import math

class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_infinite_arr(reader, key):
    start, end = 0, 1

    # find proper bound {range of numbers} ==> {end - start + 1} to search key
    # not in entire array | our goal is not to find length of array but to find key
    while reader.get(end) < key:
        newStart = end + 1
        # double the bound size
        end += (end - start + 1) * 2
        start = newStart
    
    return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if key == reader.get(mid):
            return mid
        elif key < reader.get(mid):
            end = mid - 1
        else:
            start = mid + 1
    
    return -1


if __name__ == "__main__":
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_infinite_arr(reader, key = 16))
    print(search_infinite_arr(reader, key = 28))

    reader2 = ArrayReader([1, 3, 8, 10, 15])
    print(search_infinite_arr(reader2, key = 15))
    print(search_infinite_arr(reader2, key = 200))
