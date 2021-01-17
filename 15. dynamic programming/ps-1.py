'''
Longest Palindromic Subsequence

Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

A `subsequence` is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".
'''

def find_LPS_length_helper(str, left, right):
    if left > right:
        return 0
    
    # every sequence with one element is a palindrome of length 1
    if left == right:
        return 1

    # case 1: elements at the beginning and the end are the same
    if str[left] == str[right]:
        return 2 + find_LPS_length_helper(str, left + 1, right - 1)
    
    # case 2: skip one element either from the beginning or the end
    c1 = find_LPS_length_helper(str, left + 1, right)
    c2 = find_LPS_length_helper(str, left, right - 1)

    return max(c1, c2)


def find_LPS_length(str):
    return find_LPS_length_helper(str, 0, len(str) - 1)


if __name__ == "__main__":
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))
