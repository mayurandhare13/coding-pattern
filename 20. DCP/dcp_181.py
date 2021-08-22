def isPalindrome(s, start, end) -> bool:
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


def dfs(s, start, path: list, res: list):
    if start >= len(s):
        res.append(path)
        return
    
    for end in range(start, len(s)):
        if isPalindrome(s, start, end):
            dfs(s, end + 1, path + [s[start: end + 1]], res)


def partition(s: str):
    res = []
    dfs(s, 0, [], res)

    return res


if __name__ == '__main__':
    print(partition('aab'))
