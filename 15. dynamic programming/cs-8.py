'''
Subsequence Pattern Matching

Input: string: “tomorrow”, pattern: “tor”
Output: 4
Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.
'''

def find_SPM_count_helper(str, pattern, strIndex, patIndex):
    if patIndex == len(pattern):
        return 1
    
    if strIndex == len(str):
        return 0

    c1 = 0
    if str[strIndex] == pattern[patIndex]:
        c1 = find_SPM_count_helper(str, pattern, strIndex + 1, patIndex + 1)
    
    c2 = find_SPM_count_helper(str, pattern, strIndex + 1, patIndex)

    return c1 + c2


def find_SPM_count(str, pattern):
    return find_SPM_count_helper(str, pattern, 0, 0)


if __name__ == "__main__":
    print(find_SPM_count("tomorrow", "tor"))
    print(find_SPM_count("baxmx", "ax"))
