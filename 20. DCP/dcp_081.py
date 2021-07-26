def letterCombinations(digits: str) -> list:
    numMap = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', 
        '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        
        for letter in numMap[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()


    combinations = []
    backtrack(0, [])
    return combinations


if __name__ == '__main__':
    assert letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# O(4^N * N) 
# num 7, 9 have 4 options. worst case 7, 9 combinations (7779)
# -> 2nd N costs up to N to build the combination.
