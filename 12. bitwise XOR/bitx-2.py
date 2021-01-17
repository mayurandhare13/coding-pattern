'''
Single Number

In a non-empty array of integers, every number appears twice except for one, find that single number.

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
'''

def find_single_number(arr):
    single_number = 0

    for i in arr:
        single_number ^=  i
    
    return single_number


if __name__ == "__main__":
    print(find_single_number([1, 4, 2, 1, 3, 2, 3]))
    print(find_single_number([7, 9, 7]))
