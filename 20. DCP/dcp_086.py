def minRemoveToValid(s: str) -> int:
    stack = []
    minRemove = 0
    for idx, ch in enumerate(s):
        if ch == '(':
            stack.append(idx)

        elif not stack:         # extra )
            minRemove += 1

        else:
            stack.pop()

    return minRemove + len(stack)


if __name__ == '__main__':
    assert minRemoveToValid('()())()') == 1
    assert minRemoveToValid(')(') == 2
