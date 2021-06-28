def getEditDistance(s1: str, s2: str) -> int:
    if s1 == s2:
        return 0

    if not s1:
        return len(s2)
    
    if not s2:
        return len(s1)

    if s1[0] == s2[0]:
        return getEditDistance(s1[1:], s2[1:])
    
    substitute = getEditDistance(s1[1:], s2[1:])
    delete = getEditDistance(s1[1:], s2)
    insert = getEditDistance(s1, s2[1:])

    return 1 + min(substitute, delete, insert)


if __name__ == '__main__':
    assert getEditDistance('kitten', 'sitting') == 3
    assert getEditDistance('', 'abc') == 3
    assert getEditDistance('dac', 'abc') == 2
