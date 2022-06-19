def isMatch(text: str, pattern: str) -> bool:
    if not pattern:
        return not text
    
    firstMatch = text and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (firstMatch and isMatch(text[1:], pattern)) or isMatch(text, pattern[2:])

    else:
        return firstMatch and isMatch(text[1:], pattern[1:])


def isMatchDp(text: str, pattern: str) -> bool:
    # The DP table and the string text and pattern use the same indexes i and j, but
    # dp[i][j] means the match status between text[:i] and pattern[:j], i.e.
    # dp[0][0] means the match status of two empty strings, and
    # dp[1][1] means the match status of text[0] and pattern[0]. Therefore, when
    # refering to the i-th and the j-th characters of text and pattern for updating
    # dp[i][j], we use text[i - 1] and pattern[j - 1].

    tLen, pLen = len(text), len(pattern)

    dp = [[False] * (pLen + 1) for _ in range(tLen + 1)]

    # empty text and pattern
    dp[0][0] = True

    # pattern a*, a*b* and '' string --> True
    for i in range(1, pLen + 1):
        if pattern[i-1] == '*':
            dp[0][i] = dp[0][i-2]
    
    for i in range(1, tLen + 1):
        for j in range(1, pLen + 1):
            if text[i-1] == pattern[j-1] or pattern[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            
            elif pattern[j-1] == '*':
                # 0 occurances
                # p: xa*  --> p: `x`  match  s: `xa`  (False, in this case)
                dp[i][j] = dp[i][j-2]

                # 1 or more occurances
                # p: `xa*`  match  s: `xa` --> s: `x`
                # as prev char of * (`a`) matches the current char from string
                if pattern[j-2] == text[i-1] or pattern[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            
            else:
                dp[i][j] = False
    
    return dp[tLen][pLen]


if __name__ == '__main__':
    assert isMatch('ray', 'ra.') == True
    assert isMatch('chat', '.*at') == True

    assert isMatchDp('ray', 'ra.') == True
    assert isMatchDp('chat', '.*at') == True