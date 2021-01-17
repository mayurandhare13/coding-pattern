'''
Two Single Numbers (medium)

In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
'''

def find_single_numbers(arr):
    # get XOR of all elements
    n1xn2 = 0
    for i in arr:
        n1xn2 ^= i

    # get the rightmost bit that is `1`
    # finding rightmost set bit is cuz of 1^0 = 1
    # if we find the `1`, so we know bit is differ in both numbers
    
    rightmost_set_bit = 1
    while rightmost_set_bit & n1xn2 == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    
    num1, num2 = 0, 0
    for num in arr:
        if num & rightmost_set_bit != 0:    # bit is set
            num1 ^= num
        else:                               # bit is not set
            num2 ^= num

    return [num1, num2]


if __name__ == "__main__":
    print(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    print(find_single_numbers([2, 1, 3, 2]))
