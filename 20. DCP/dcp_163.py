def evalRPN(tokens: list) -> int:
    operations = {
        '+' : lambda a, b: a + b,
        '-' : lambda a, b: a - b,
        '*' : lambda a, b: a * b,
        '/' : lambda a, b: a // b
    }

    stack = []
    for token in tokens:
        if token in operations:
            num2 = stack.pop()
            num1 = stack.pop()
            operation = operations[token]
            stack.append(operation(num1, num2))

        else:
            stack.append(token)
    
    return stack.pop()


if __name__ == '__main__':
    assert evalRPN([5, 3, '+']) == 8
    assert evalRPN([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5
