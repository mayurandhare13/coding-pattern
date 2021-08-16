class Node:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.finished = False
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = Node()


    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node(ch)

            node.count += 1             
            node = node.children[ch]

        node.finished = True


    def uniquePrefix(self, word):
        node = self.root
        prefix = ''

        for ch in word:
            if node.count == 1:
                return prefix

            node = node.children[ch]
            prefix += ch

        return prefix


# O(n) time
def shortestUniquePrefix(lst):
    trie = Trie()
    for word in lst:
        trie.insert(word)

    return [trie.uniquePrefix(word) for word in lst]


if __name__ == '__main__':
    lst = ['dog', 'cat', 'apple', 'apricot', 'fish']
    assert shortestUniquePrefix(lst) == ['d', 'c', 'app', 'apr', 'f']
