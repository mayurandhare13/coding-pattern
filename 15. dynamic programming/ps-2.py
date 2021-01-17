'''
Longest Palindromic Substring

Input: = "cddpd"
Output: 3
Explanation: LPS is "dpd".
'''

def find_LPS_length_helper(str, left, right):
    if left > right:
        return 0

    # every string with one character is a palindrome
    if left == right:
        return 1

    # case 1: elements at the beginning and the end are the same
    if str[left] == str[right]:
        remaining_length = right - left - 1
        if remaining_length == find_LPS_length_helper(str, left + 1, right - 1):
            return remaining_length + 2
    
    # case 2: skip one element either from the beginning or the end
    c1 = find_LPS_length_helper(str, left + 1, right)
    c2 = find_LPS_length_helper(str, left, right - 1)
    return max(c1, c2)


def find_LPS_length(str):
    return find_LPS_length_helper(str, 0, len(str) - 1)


if __name__ == "__main__":
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("pqr"))
