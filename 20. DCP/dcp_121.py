# O(2^min(n, k)) time
def palindromeK(S, K):
    if len(S) <= 1:
        return True
    
    while S[0] == S[-1]:
        S = S[1:-1]
        if len(S) <= 1:
            return True
    
    if K == 0:
        return False
    
    return palindromeK(S[1:], K - 1) or palindromeK(S[:-1], K - 1)


# ------------------------------------------------------------------


def palindromeK2(S, K):
    return len(S) - longestPalindromicSubsequence(S) <= K


# O(n^2) time and space
def longestPalindromicSubsequence(S):
    n = len(S)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1    # diagonal

        for j in range(i + 1, n):
            if S[i] == S[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]

            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


if __name__ == '__main__':
    assert palindromeK2('waterrfetawx', 2)
    assert palindromeK2('racecar', 1)
