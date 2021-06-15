def staircase(n):
    # if 0 or 1 steps then only 1 way
    if n <= 1:
        return 1
    
    # if 2 steps --> {1, 1}, {2}
    if n == 2:
        return 2

    return staircase(n-1) + staircase(n-2)


# X = {1, 3, 4}, then f(n) = f(n - 1) + f(n - 3) + f(n - 4)
# very slow (O(|X|^N))
def stairCase(n: int, X: dict) -> int:
    if n < 0:
        return 0
    
    elif n == 0:
        return 1

    elif n in X:
        return 1 + sum(stairCase(n-x, X) for x in X if x < n)

    else:
        return sum(stairCase(n-x, X) for x in X if x < n)


# O(N * |X|) time and O(N) space
def stairCase2(n: int, X: dict) -> int:
    dp = [0 for _ in range(n+1)]
    dp[0] = 1       # 0 steps

    for i in range(n+1):
        dp[i] += sum(dp[i-x] for x in X if i > x)
        dp[i] += 1 if i in X else 0
    
    return dp[-1]


def stairCaseCombinations(n: int, X: dict) -> list[list]:
    if n < min(X):
        return []

    combinations = []
    # we want valid steps for combinations
    # so we iterate over steps
    for x in X:
        if n == x:
            combinations.append([x])
        
        elif n > x:
            combos = stairCaseCombinations(n-x, X)
            for c in combos:
                combinations.append([x] + c)
    
    return combinations


if __name__ == '__main__':
    assert staircase(4) == 5
    assert stairCase(5, {1, 3, 4}) == 6
    assert stairCase2(5, {1, 3, 4}) == 6
    assert stairCaseCombinations(5, {1, 3, 4}) == \
        [[1, 1, 1, 1, 1], [1, 1, 3], [1, 3, 1], [1, 4], [3, 1, 1], [4, 1]]
