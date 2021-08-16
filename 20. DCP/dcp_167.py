def isPalindrome(word: str) -> bool:
    return word == word[::-1]


# O(n^2 * c)    c = length of longest word (isPalindrome check)
def palindromePairs(words: list):
    result = []

    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            
            if isPalindrome(word1 + word2):
                result.append((i, j))
    
    return result

# ---------------------------------------------
# O(n * c2)
def palindromePairs2(words: list):
    d = {}
    for i, word in enumerate(words):
        d[word] = i
    
    result = []

    for i, word in enumerate(words):
        for charI in range(len(word)):
            prefix, postfix = word[:charI], word[charI:]
            reversePrefix, reversePostfix = prefix[::-1], postfix[::-1]

            if isPalindrome(prefix) and reversePostfix in d:
                if i != d[reversePostfix]:
                    result.append((d[reversePostfix], i))

            if isPalindrome(postfix) and reversePrefix in d:
                if i != d[reversePrefix]:
                    result.append((i, d[reversePrefix]))            
    
    return result


# aabc  a cba

if __name__ == '__main__':
    assert palindromePairs(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]
    assert palindromePairs2(["code", "edoc", "da", "d"]) == [(1, 0), (0, 1), (2, 3)]
