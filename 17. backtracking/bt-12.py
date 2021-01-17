'''
Word Break

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
'''

def word_break_helper(s, wordDict, start):
    if start == len(s):
        return True
    
    for i in range(start+1, len(s)+1):
        word = s[start : i]
        if word in wordDict:
            if word_break_helper(s, wordDict, i):
                return True
    
    return False


def word_break(s, wordDict):
    return word_break_helper(s, set(wordDict), 0)


if __name__ == "__main__":
    print(word_break("applepenapple", ["apple", "pen"]))
    print(word_break("leetcode", ["leet", "code"]))
    print(word_break("aaaaaaa", ["aaa", "aaaa"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
