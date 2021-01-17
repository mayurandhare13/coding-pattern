'''
Word Break II

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

NOTE cat & cats, and & sand, have the prefixes. 
If we use bt-12, then some of these words won't found
'''

def word_break_helper(s, wordDict):
    results = []
    if not s:
        return [[]] # return empty list

    for i in range(1, len(s)+1):
        word = s[:i]
        if word in wordDict:
            # move forwards to break the postfix into words
            subsequence = word_break_helper(s[i:], wordDict)
            for subseq in subsequence:
                results.append([word] + subseq)
    
    return results


def word_break(s, wordDict):
    results = word_break_helper(s, set(wordDict))
    return [" ".join(word) for word in results]


if __name__ == "__main__":
    print(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    print(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
