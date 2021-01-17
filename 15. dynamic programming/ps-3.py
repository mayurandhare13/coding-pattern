'''
Count of Palindromic Substrings

Input: = "cddpd"
Output: 7
Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".
'''

def isPalindrome(str, start, end):
    while start <= end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    
    return True


def count_LPS_length_helper(dp, str, left, right):
    if left > right:
        return 0

    # every string with one character is a palindrome
    if left == right:
        return 1

    if dp[left][right] == -1:
        # case 1: elements at the beginning and the end are the same
        totalPSCount = 0
        if isPalindrome(str, left, right):
            totalPSCount += 1
        
        # case 2: skip one element either from the beginning or the end
        totalPSCount += count_LPS_length_helper(dp, str, left + 1, right)
        totalPSCount += count_LPS_length_helper(dp, str, left, right - 1)
        
        # because of the above two recursive calls, since we have counted twice all 
        # palindromes from "startIndex+1" to "endIndex-1", let's subtract one count
        totalPSCount -= count_LPS_length_helper(dp, str, left + 1, right - 1)

        dp[left][right] = totalPSCount

    return dp[left][right]


def count_LPS_length(str):
    n = len(str)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return count_LPS_length_helper(dp, str, 0, len(str) - 1)


if __name__ == "__main__":
    print(count_LPS_length("cddpd"))
    print(count_LPS_length("abdbca"))
    print(count_LPS_length("pqr"))
