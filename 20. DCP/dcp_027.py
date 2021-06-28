def validBrackets(brackets: str) -> bool:
    bracketsMap = {
        ')':'(',
        ']':'[',
        '}':'{',
    }

    stack = []
    for b in brackets:
        if b in bracketsMap:
            topElement = stack.pop() if stack else '#'
            if bracketsMap[b] != topElement:
                return False

        else:
            stack.append(b)
    
    return not stack


if __name__ == '__main__':
    assert validBrackets('')
    assert validBrackets('{}')
    assert validBrackets('([])')
    assert validBrackets('([])[]({})')
    assert not validBrackets('(')
    assert not validBrackets(']')
    assert not validBrackets('((()')
    assert not validBrackets('([)]')
