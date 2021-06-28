def longestPath(input: str) -> int:
    maxLen = 0
    pathLen = {0: 0}    # base for Root dir

    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)

        if '.' in name:
            maxLen = max(maxLen, pathLen[depth] + len(name))
        else:
            # pathLen[depth]    --> Parent
            # pathLen[depth+1]  --> Child
            # +1                --> `/` char between dirs/file 
            pathLen[depth+1] = pathLen[depth] + len(name) + 1

    return maxLen


if __name__ == '__main__':
    assert longestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
