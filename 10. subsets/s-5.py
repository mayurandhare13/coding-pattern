'''
Balanced Parentheses (hard)

For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Input: N=2
Output: (()), ()()
'''

from collections import deque


class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))

    while queue:
        ps = queue.popleft()

        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.str)
        else:
            if ps.openCount < num:
                queue.append(ParenthesesString(
                    ps.str + "(", ps.openCount + 1, ps.closeCount
                ))
            if ps.closeCount < ps.openCount:
                queue.append(ParenthesesString(
                    ps.str + ")", ps.openCount, ps.closeCount + 1
                ))
    
    return result


if __name__ == "__main__":
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))
