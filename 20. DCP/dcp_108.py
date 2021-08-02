# O(n^2)
def sameString(s1, s2) -> bool:
    if len(s1) != len(s2):
        return False

    s = s1 + s1
    return s2 in s


def sameString2(s1, s2) -> bool:
    s1Len = len(s1)
    s2Len = len(s2)

    if s1Len != s2Len:
        return False

    for i in range(s1Len):
        if all( s1[(i+j) % s1Len] == s2[j] 
                    for j in range(s2Len)):
            return True

    return False


if __name__ == '__main__':
    assert sameString('abcde', 'cdeab')
    assert not sameString('abc', 'acb')

    assert sameString2('abcde', 'cdeab')
    assert not sameString2('abc', 'acb')
