'''
Longest Common Subsequence

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 5
Explanation: The longest common subsequence is "psspt".
'''

def find_LCS_lengths_helper(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0

    if s1[index1] == s2[index2]:
        return 1 + find_LCS_lengths_helper(s1, s2, index1 + 1, index2 + 1)
    
    c1 = find_LCS_lengths_helper(s1, s2, index1 + 1, index2)
    c2 = find_LCS_lengths_helper(s1, s2, index1, index2 + 1)
    
    return max(c1, c2)


def find_LCS_lengths(s1, s2):
    return find_LCS_lengths_helper(s1, s2, 0, 0)


if __name__ == "__main__":
    print(find_LCS_lengths("abdca", "cbda"))
    print(find_LCS_lengths("passport", "ppsspt"))
