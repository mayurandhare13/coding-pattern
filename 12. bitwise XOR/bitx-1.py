'''
Given an array of (n−1) integers in the range from 1 to n, find the one number that is missing from the array.

Input: 1, 5, 2, 6, 4
Answer: 3
'''


def find_missing_number(arr):
    n = len(arr) + 1

    # XOR all values 1 to n
    x1 = 1
    for i in range(2, n+1):
        x1 = x1 ^ i

    # XOR all values for arr
    x2 = 0
    for num in arr:
        x2 = x2 ^ num

    return x1 ^ x2


def find_missing_number2(arr):

    ans = len(arr) + 1

    for key, val in enumerate(arr):
        ans ^= (key+1) ^ val
    
    return ans


if __name__ == "__main__":
    print(find_missing_number([1, 5, 2, 6, 4]))
    print(find_missing_number([5, 2, 6, 4, 3]))
    print(find_missing_number2([1, 5, 2, 6, 4]))
    print(find_missing_number2([5, 2, 6, 4, 3]))
