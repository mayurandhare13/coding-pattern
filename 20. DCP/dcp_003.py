def calculate(s: str):
    sum = 0
    sign = 1
    stack = []

    for i in range(len(s)):
        
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            
            i -= 1
            sum += sign * num
        
        elif s[i] == '+':
            sign = 1
        
        elif s[i] == '-':
            sign = -1
        
        elif s[i] == '(':
            stack.append(sum)
            stack.append(sign)

            sign, sum = 1, 0

        elif s[i] == ')':
            operand = stack.pop()
            last_sum = stack.pop()

            sum = last_sum + operand * sum
    
    return sum


if __name__ == '__main__':
    s = "(1 + (4+5+2) -3 ) + (6+8)"
    res = calculate(s)
    print(res)
