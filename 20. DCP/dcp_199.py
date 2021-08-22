def balanceParentheses(s: str) -> str:
    parentheses = []
    openBraces = 0

    for ch in s:
        if ch == '(':
            openBraces += 1
            parentheses.append(ch)

        else:
            if not openBraces:
                parentheses.append('(')
            else:
                openBraces -= 1
            parentheses.append(ch)

    while openBraces:
        parentheses.append(')')
        openBraces -= 1

    return ''.join(parentheses)



if __name__ == '__main__':
    assert balanceParentheses('(()') == '(())'
    assert balanceParentheses('))()(') == '()()()()'
