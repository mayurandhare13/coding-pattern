'''
Alien Dictionary (hard)
There is a "dictionary" containing words from an alien language for which we don’t know the ordering of the characters. Write a method to find the correct order of characters in the alien language.

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are "sorted lexicographically" by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:
 
1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
 
From the above two points, we can conclude that the correct character order is: "bac"
'''

from collections import deque


def find_order(words):
    sortedOrder = []
    if len(words) <= 0:
        return ""

    # 1. initialize indegrees and graph
    indegrees = {}
    graph = {}
    for word in words:
        for char in word:
            indegrees[char] = 0
            graph[char] = []

    # 2. build graph
    for i in range(0, len(words) - 1):
        # find ordering of chars from adjacent words
        w1, w2 = words[i], words[i+1]
        for j in range(min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                indegrees[child] += 1
                break   # we found the order between 2 word's char
    
    # 3. find sources
    sources = deque()
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)

    # 4. sorting
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sources.append(child)

    # if sortedOrder doesn't contain all words, then cyclic dependency
    return ''.join(sortedOrder) if len(sortedOrder) == len(indegrees) else ""


if __name__ == "__main__":
    print(find_order(["ba", "bc", "ac", "cab"]))
    print(find_order(["cab", "aaa", "aab"]))
    print(find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))
