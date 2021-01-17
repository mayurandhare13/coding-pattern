'''
Palindromic Partitioning
Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

Input: = "cddpd"
Output: 2
Explanation: Palindrome pieces are "c", "d", "dpd".
'''

def isPalindrome(st, x, y):
    while x <= y:
        if st[x] != st[y]:
            return False
        x += 1
        y -= 1
    
    return True


def find_MPP_cuts_helper(st, start, end):
    # if string is already a palindrome
    if start >= end or isPalindrome(st, start, end):
        return 0

    # maximum cuts we need is `length - 1` pieces
    minimum_cuts = end - start
    for i in range(start, end):
        if isPalindrome(st, start, i):
            minimum_cuts = min(minimum_cuts,
                                1 + find_MPP_cuts_helper(st, i + 1, end))
    
    return minimum_cuts


def find_MPP_cuts(st):
    return find_MPP_cuts_helper(st, 0, len(st) - 1)


if __name__ == "__main__":
    print(find_MPP_cuts("cddpd"))
    print(find_MPP_cuts("abdbca"))
    print(find_MPP_cuts("pqr"))
    print(find_MPP_cuts("pp"))
