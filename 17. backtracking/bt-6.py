'''
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParentheses(num):
    
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * num:
            results.append(S)
            return
        
        if left < num:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)
    
    results = []
    backtrack()
    return results


if __name__ == "__main__":
    print(generateParentheses(3))
