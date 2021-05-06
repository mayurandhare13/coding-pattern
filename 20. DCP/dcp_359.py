from collections import defaultdict

DIGIT_MAP = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
}

def getCharCounts(string):
    charFreqMap = defaultdict(int)
    for c in string:
        charFreqMap[c] += 1
    
    return charFreqMap


def useDigit(letterFreq, digitFreq):
    for c in digitFreq:
        if c not in letterFreq or letterFreq[c] < digitFreq[c]:
            return letterFreq, 0

    # found one digit
    for c in digitFreq:
        letterFreq[c] -= digitFreq[c]
    
    # there can be more
    letterFreq, uses = useDigit(letterFreq, digitFreq)
    return letterFreq, uses + 1


def getSortedNumber(string):
    letterFreq = getCharCounts(string)
    result = 0

    for i in range(10):
        digit = DIGIT_MAP[i]
        digitFreq = getCharCounts(digit)
        letterFreq, uses = useDigit(letterFreq, digitFreq)

        while uses > 0:
            result = result * 10 + i
            uses -= 1

    return result


if __name__ == '__main__':
    print(getSortedNumber('niesevehrtfeev'))     # 357
    print(getSortedNumber('nienienn'))           # 99
    print(getSortedNumber('enieniennon'))        # 199