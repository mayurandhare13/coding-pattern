def isNegativeReal(s: str):
    return s.startswith('-') and isPositiveReal(s[1:])


def isNegativeInteger(s: str):
    return s.startswith('-') and isPositiveInteger(s[1:])


def isNegativeNumber(s: str):
    return isNegativeInteger(s) or isNegativeReal(s)


def isPositiveInteger(s: str):
    return s.isdigit()


def isPositiveReal(s: str):
    if s.count('.') != 1:
        return False
    
    integerPart, decimalPart = s.split('.')

    return isPositiveInteger(integerPart) and \
        isPositiveInteger(decimalPart)


def isPositiveNumber(s: str):
    return isPositiveInteger(s) or isPositiveReal(s)


def isScientificNumber(s: str):
    if s.count('e') != 1:
        return False
    
    beforeE, afterE = s.split('e')
    return (isPositiveNumber(beforeE) or isNegativeNumber(beforeE)) and \
        (isPositiveNumber(afterE) or isNegativeNumber(afterE))


def isNumber(s: str) -> bool:
    return isPositiveNumber(s) or isNegativeNumber(s) or isScientificNumber(s)


if __name__ == '__main__':
    assert isNumber('10')
    assert isNumber('-10')
    assert isNumber('10.1')
    assert isNumber('-10.1')
    assert isNumber('1e5')
    assert not isNumber('a')
    assert not isNumber('x 1')
    assert not isNumber('a -2')
    assert not isNumber('-')
