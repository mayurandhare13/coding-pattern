from functools import lru_cache

@lru_cache(maxsize=None)
def decodeWaysHelper(s: str, index: int) -> int:
    if index == len(s) or index == len(s)-1:
        return 1

    if s[index] == '0':
        return 0

    # if index == len(s)-1:
        # return 1

    ans = decodeWaysHelper(s, index+1)
    if int(s[index : index + 2]) <= 26:
        ans += decodeWaysHelper(s, index + 2)

    return ans


def decodeWays(s: str) -> int:
    return decodeWaysHelper(s, 0)



def decodeWaysIterative(s: str) -> int:
    size = len(s)
    dp = [0] * (size+1)
    dp[0] = 1

    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, size+1):
        if s[i-1] != '0':
            dp[i] = dp[i - 1]
        
        twoDigit = int(s[i - 2 : i])
        if twoDigit >= 10 and twoDigit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[size]



if __name__ == '__main__':
    assert decodeWays('111') == 3
    assert decodeWays('226') == 3
    assert decodeWays('2326') == 4

    assert decodeWaysIterative('111') == 3
    assert decodeWaysIterative('226') == 3
    assert decodeWaysIterative('2326') == 4
