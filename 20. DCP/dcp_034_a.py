from sys import maxsize

def findMinInsertionRec(s, l, h):
    if l > h:
        return maxsize
    
    # 1 char
    if l == h:
        return 0
    # 2 chars
    if l == h - 1:
        return 0 if s[l] == s[h] else 1

    if s[l] == s[h]:
        return findMinInsertionRec(s, l+1, h-1)
    
    return 1 + min (
                    findMinInsertionRec(s, l+1, h),
                    findMinInsertionRec(s, l, h-1)
                )



# find longest common subsequence
def lcs(s1, s2):
    l1, l2 = len(s1), len(s2)

    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[l1][l2]


def findMinInsertion(string):
    n = len(string)
    return n - lcs(string, string[::-1])


if __name__ == '__main__':
    assert findMinInsertion('race') == 3
    assert findMinInsertion('google') == 2
    
    assert findMinInsertionRec('race', 0, 3) == 3
    assert findMinInsertionRec('google', 0, 5) == 2
