def calculate(s: str):
    total = 0
    sign = 1
    stack = []

    for i in range(len(s)):
        
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            
            i -= 1
            total += sign * num

        if s[i] == '+':
            sign = 1
        
        elif s[i] == '-':
            sign = -1
        
        elif s[i] == '(':
            stack.append(total)
            stack.append(sign)

            sign, total = 1, 0

        elif s[i] == ')':
            operand = stack.pop()
            last_total = stack.pop()

            total = last_total + operand * total
    
    return total


if __name__ == '__main__':
    s = "(1 + (4+5+2) -3 ) + (6+8)"
    res = calculate(s)
    print(res)

    print(calculate("-1 + (2 + 3)"))
