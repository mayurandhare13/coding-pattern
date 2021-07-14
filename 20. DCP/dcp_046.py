def palindromeSubstringHelper(s, left, right):
    if left > right:
        return 0

    if left == right:
        return 1
    
    if s[left] == s[right]:
        remainLen = right - left - 1
        if remainLen == palindromeSubstringHelper(s, left+1, right -1):
            return remainLen + 2
    
    c1 = palindromeSubstringHelper(s, left+1, right)
    c2 = palindromeSubstringHelper(s, left, right-1)
    
    return max(c1, c2)


def palindromeSubstring(s):
    return palindromeSubstringHelper(s, 0, len(s) - 1)

#--------------------------------------------------------------

def longestPalindrome(s):
    #  palindrome mirrors around its center
    #  O(n^2)

    if not s or len(s) < 1:
        return ''

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandAround(s, i, i)        # odd
        len2 = expandAround(s, i, i+1)      # even

        length = max(len1, len2)
        if length > (end - start):
            start = i - (length - 1) // 2
            end = i + length // 2

    return s[start : end+1]


def expandAround(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return right - left - 1


if __name__ == '__main__':
    assert palindromeSubstring('aabcdcb') == 5
    assert longestPalindrome('aabcdcb') == 'bcdcb'

    assert palindromeSubstring('banana') == 5
    assert longestPalindrome('banana') == 'anana'
