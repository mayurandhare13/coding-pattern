from collections import deque

ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

def getNeighbors(word: str) -> list:
    result = []
    for i in range(len(word)):
        for c in ALPHABETS:
            w = word[:i] + c + word[i+1:]
            result.append(w)
    
    return result


def wordLadder(beginWord, endWord, wordList: list):
    words = set(wordList)
    queue = deque([beginWord])
    length = 0

    while queue:
        size = len(queue)
        length += 1

        for i in range(size):
            word = queue.popleft()
            if word == endWord:
                return length

            neighbors = getNeighbors(word)
            for nei in neighbors:
                if nei in words:
                    words.remove(nei)
                    queue.append(nei)

    return 0


if __name__ == '__main__':
    assert wordLadder('hit', 'cog', wordList = ["hot","dot","dog","lot","log","cog"]) == 5
