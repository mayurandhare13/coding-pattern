# O(n) time and space
def firstOcuuring(s: str):
    seen = set()
    for c in s:
        if c in seen:
            return c

        seen.add(c)

    return None


# O(n) time and O(1) space
def firstOcuuring2(s: str):
    checker = 0
    for c in s:
        val = ord('z') - ord(c)
        if checker & (1 << val) != 0:
            return c

        checker = checker | (1 << val)

    return None


if __name__ == '__main__':
    assert firstOcuuring('acbbac') == 'b'
    assert firstOcuuring('abcdef') == None

    assert firstOcuuring2('acbbac') == 'b'
    assert firstOcuuring2('abcdef') == None
