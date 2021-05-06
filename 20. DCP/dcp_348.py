class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.mid = None
        self.right = None
        self.endWord = False


def insert(node, word, index):
    if node is None:
        node = Node(word[index])

    if index < len(word) - 1:
        if word[index] < node.char:
            node.left = insert(node.left, word, index)
        
        elif word[index] > node.char:
            node.right = insert(node.right, word, index)
        
        else:
            node.mid = insert(node.mid, word, index + 1)

    else:
        node.endWord = True
    
    return node


def builtTree(wordList):
    root = None

    for word in wordList:
        root = insert(root, word, 0);

    return root


def search(root, word):
    prev = root

    for c in word:
        # searching for appropriate node
        while root and root.char != c:
            prev = root
            root = root.left if c < root.char else root.right
        
        # if character matches follow the mid link
        if root: 
            prev = root
            root = root.mid
        
        else: 
            return False

    return prev.endWord # if the node is marked then string is found


if __name__ == '__main__':
    wordList = ['cat', 'up', 'cats', 'bug']
    root = builtTree(wordList)

    print(search(root, 'bug'))

