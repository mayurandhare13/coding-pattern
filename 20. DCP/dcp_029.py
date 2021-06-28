def encode(s: str) -> str:
    sLen = len(s)
    arr = []
    i = 0
    while i < sLen:
        count = 1
        currChar = s[i]
        while i+1 < sLen and s[i] == s[i+1]:
            count += 1
            i += 1

        arr.append(str(count))
        arr.append(currChar)
        i += 1
    
    return ''.join(arr)


def decode(s: str) -> str:
    arr = []
    i = 0
    while i < len(s):
        arr.append(s[i+1] * int(s[i]))
        i += 2
    
    return ''.join(arr)


if __name__ == '__main__':
    assert encode('AAAABBBCCDAA') == '4A3B2C1D2A'
    assert decode('4A3B2C1D2A') == 'AAAABBBCCDAA'

    assert encode('ABBCCCDDDD') == '1A2B3C4D'
    assert decode('1A2B3C4D') == 'ABBCCCDDDD'
