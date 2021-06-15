# brute force
def getSuggestions(wordList: list, prefix: str) -> list:
    size = len(prefix)
    return [
        word for word in wordList if word[:size] == prefix
    ]

# -----------------------------------------------------------

class TrieNode:
    def __init__(self, val=None) -> None:
        self.val = val
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    

    def insert(self, word: str) -> None:
        current = self.root
        
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode(ch)

            current = current.children[ch]
        
        current.isEnd = True


    def search(self, word: str) -> bool:
        current = self.root

        for ch in word:
            if ch not in current.children:
                return False
            
            current = current.children[ch]
        
        return current.isEnd


    def startsWith(self, prefix: str) -> list:
        wordList = []
        explore = []

        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return []
            
            current = current.children[ch]
        
        # make tuple of prefix nodes
        for key in current.children:
            explore.append((prefix + key, current.children[key]))
        
        while len(explore) > 0:
            prefix, node = explore.pop()

            if node.isEnd:
                wordList.append(prefix)

            # prefix of word can be a separate word
            # words = ['ant', 'antenna']
            for child in node.children:
                explore.append((prefix + child, node.children[child]))
        
        return wordList
    
    def __str__(self):
        return str(self.children)


if __name__ == '__main__':
    assert getSuggestions(['dog', 'deer', 'deal'], 'de') == ['deer', 'deal']

    obj = Trie()
    obj.insert('dog')
    obj.insert('doge')
    obj.insert('deer')
    obj.insert('deal')
    obj.insert('dealer')

    assert obj.startsWith('de') == ['deal', 'dealer', 'deer']
