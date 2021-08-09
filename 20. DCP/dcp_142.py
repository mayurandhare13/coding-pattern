# * ->  try every path (so with count [], count - 1 [)], and count + 1 [(])

def balanced(string, count = 0):
    if not string and count == 0:
        return True
    
    c = count
    for i, char in enumerate(string):
        if char == '(':
            c += 1
        
        elif char == ')':
            c -= 1
        
        elif char == '*':
            return balanced(string[i + 1 : ], c) or \
                balanced(string[i + 1 : ], c + 1) or \
                balanced(string[i + 1 : ], c - 1)

        if c < 0:
            return False

    return c == 0


def balanced2(string) -> bool:
    low, high = 0, 0

    for char in string:
        # increment both low and high - they both contribute to the counts of unbalanced open parentheses
        if char == '(':
            low += 1
            high += 1
        
        # decrement both low and high - we have one less unbalanced open parenthesis
        elif char == ')':
            low = max(low - 1, 0)
            high -= 1

        # decrement low but increment high, it could mean either a `)` or `(`        
        elif char == '*':
            low = max(low - 1, 0)
            high += 1
        
        if high < 0:
            return False

    return low == 0



if __name__ == '__main__':
    assert balanced('()*') == True
    assert balanced('(*)') == True
    assert balanced(')*(') == False
