'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

'''

def maxLength(arr: list[str]) -> int:
    best = 0
    result = ['']

    for s in arr:
        for r in result:
            tmp = r + s
            if len(tmp) != len(set(tmp)):
                continue
            result.append(tmp)
            best = max(best, len(tmp))
    
    return best

# -----------------------------------------------------

def dfs(arr: list, pos: int, word: str) -> int:
    if len(word) != len(set(word)):
        return 0
    
    best = len(word)
    for i in range(pos, len(arr)):
        best = max(best, dfs(arr, i + 1, word + arr[i]))
    
    return best


def maxLengthDFS(arr: list[str]) -> int:
    return dfs(arr, 0, '')

# -----------------------------------------------------



def word2bits(opt: set[int], word: str):
    bits = 0
    for c in word:
        mask = 1 << (ord(c) - 97)
        # duplicate chars found
        # although set would take care of this.
        if bits & mask:
            return

        bits |= mask
    
    # store the len of word in ununsed space 26 -> 31
    # alphabets will be stored at 0 -> 25
    opt.add(bits | (len(word) << 26))


def dfsBits(opt: list[int], pos: int, res: int):
    # separate parts of bitset into string bits and its len
    oldchars = res & ((1 << 26) - 1)
    oldlen = res >> 26

    best = oldlen

    for i in range(pos, len(opt)):
        newchars = opt[i] & ((1 << 26) - 1)
        newlen = opt[i] >> 26

        # If the two bitsets overlap, skip to the next result
        if newchars & oldchars:
            continue

        newres = oldchars | newchars | ((oldlen + newlen) << 26)
        best = max(best, dfsBits(opt, i + 1, newres))
    
    return best



def maxLengthBitDFS(arr: list[str]) -> int:
    # preprocess convert words to bitsets
    opt = set()
    for word in arr:
        word2bits(opt, word)

    optlist = list(opt)
    return dfsBits(optlist, 0, 0)


if __name__ == '__main__':
    assert maxLength(["cha","r","act","ers"]) == 6
    assert maxLengthDFS(["cha","r","act","ers"]) == 6
    assert maxLengthBitDFS(["cha","r","act","ers"]) == 6
