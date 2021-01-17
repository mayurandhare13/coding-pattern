'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

def letter_combinations(digits):
    phone = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            }


    def backtrack(combination, next_digit):
        if len(next_digit) == 0:
            results.append(combination)
            return
        
        for letter in phone[next_digit[0]]:
            ''' This also works
            combination = combination + letter
            backtrack(combination, next_digit[1:])
            combination = combination[:-1]
            '''
            backtrack(combination + letter, next_digit[1:])

    results = []
    backtrack('', digits)
    return results


if __name__ == "__main__":
    print(letter_combinations('23'))
