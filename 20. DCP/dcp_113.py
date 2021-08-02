# O(n) space
def reverseSentence(string: str) -> str:
    words = string.split(' ')
    return ' '.join(reversed(words))

# ----------------------------------------


def reverseString(l, start, end):
    while start < end:
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1

def reverseSentenceOpt(string: str) -> str:

    stringList = list(string)
    # first reverse entire string
    reverseString(stringList, 0, len(stringList) - 1)

    start = 0
    for end in range(len(stringList)):
        if stringList[end] == ' ':
            reverseString(stringList, start, end - 1)
            start = end + 1

    reverseString(stringList, start, len(stringList) - 1)

    string = ''.join(stringList)
    return string

if __name__ == '__main__':
    assert reverseSentence('hello world here') == 'here world hello'
    assert reverseSentenceOpt('hello world here') == 'here world hello'
