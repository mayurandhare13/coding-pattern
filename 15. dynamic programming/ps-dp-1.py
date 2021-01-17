'''
Longest Palindromic Subsequence

The two changing values to our recursive function are the two indexes, startIndex and endIndex. Therefore, we can store the results of all the subproblems in a two-dimensional array. (Another alternative could be to use a hash-table whose key would be a string (startIndex + “|” + endIndex))
'''

def find_LPS_length_helper(dp, str, left, right):
    if left > right:
        return 0
    
    # every sequence with one element is a palindrome of length 1
    if left == right:
        return 1

    if dp[left][right] == -1:
        # case 1: elements at the beginning and the end are the same
        if str[left] == str[right]:
            dp[left][right] = 2 + find_LPS_length_helper(dp, str, left + 1, right - 1)
        else:
            # case 2: skip one element either from the beginning or the end
            c1 = find_LPS_length_helper(dp, str, left + 1, right)
            c2 = find_LPS_length_helper(dp, str, left, right - 1)

            dp[left][right] = max(c1, c2)

    return dp[left][right]


def find_LPS_length(str):
    n = len(str)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LPS_length_helper(dp, str, 0, len(str) - 1)


if __name__ == "__main__":
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))
