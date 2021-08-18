from collections import Counter

def oneVoneMap(S1, S2):
    if len(S1) != len(S2):
        return False

    s1Count = Counter(S1).keys()
    s2Count = Counter(S2).keys()

    return len(s1Count) == len(s2Count)


if __name__ == '__main__':
    assert oneVoneMap('abc', 'bcd')
    assert oneVoneMap('abcc', 'bbcd')
    assert not oneVoneMap('foo', 'bar')
