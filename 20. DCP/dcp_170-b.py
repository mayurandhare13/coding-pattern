from sys import maxsize

ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

def getNeighbors(word: str, words: set, seen: set) -> list:
    result = []
    for i in range(len(word)):
        for c in ALPHABETS:
            w = word[:i] + c + word[i+1:]
            if w in words and w not in seen:
                result.append(w)
    
    return result


def helper(startWord, endWord, words: set, path: list, seen: set):
    if startWord == endWord:
        return path
    
    neighbors = getNeighbors(startWord, words, seen)
    minPath = []
    minLength = maxsize

    for nei in neighbors:
        seen.add(nei)
        newPath = helper(nei, endWord, words, path + [nei], seen)

        if newPath and len(newPath) < minLength:
            minLength = len(newPath)
            minPath = newPath

        seen.remove(nei)
    
    return minPath


def wordLadder(start, end, words: set):
    return helper(start, end, words, [start], {start})


if __name__ == '__main__':
    assert wordLadder('hit', 'cog', words = ("hot", "dot", "dog", "lot", "log", "cog")) == ['hit', 'hot', 'dot', 'dog', 'cog']

    assert wordLadder('dog', 'cat', words = ("dot", "dop", "dat", "cat")) == ["dog", "dot", "dat", "cat"]
