'''
Letter Tile Possibilities

You have `n` tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
'''

def numTilesPossibilities(tiles):
    result = set()

    # dfs
    def backtrack(path, tiles):
        if path and path is not result:
            result.add(path)
        
        for i in range(len(tiles)):
            backtrack(path+tiles[i], tiles[:i] + tiles[i+1:])


    backtrack('', tiles)
    return result


def numTilesPossibilities2(tiles):
    subset = ['']
    for ch in tiles:
        _len = len(subset)
        for i in range(_len):
            _set = list(subset[i])
            _set.append(ch)
            subset.append(''.join(_set))
    
    return subset


if __name__ == "__main__":
    print(numTilesPossibilities("AAB"))
    print(numTilesPossibilities2("AAB"))
    print(len(numTilesPossibilities("AAABBC")))
    print(numTilesPossibilities("V"))
