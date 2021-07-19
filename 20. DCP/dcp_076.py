def minDeletion(strs: list[str]) -> int:
    deletes = 0
    rows = len(strs)
    cols = len(strs[0])

    for j in range(cols):
        for i in range(rows - 1):
            if strs[i][j] > strs[i+1][j]:
                deletes += 1
                break

    return deletes


def minDeletion2(strs: list[str]) -> int:
    deletes = 0
    rows = len(strs)
    cols = len(strs[0])

    # used to check if rows in prev col is sorted.
    # if sorted then we do not delete the current col
    isSorted = [0] * (rows - 1)

    for j in range(cols):
        isSorted2 = isSorted[:]

        for i in range(rows - 1):
            if strs[i][j] > strs[i+1][j] and isSorted[i] == 0:
                deletes += 1
                break
            isSorted2[i] |= strs[i][j] < strs[i+1][j]

        else:
            isSorted = isSorted2

    return deletes



if __name__ == '__main__':
    assert minDeletion(['ca', 'bb', 'ac']) == 1
    assert minDeletion(['a', 'b', 'c', 'd', 'e', 'f']) == 0
    assert minDeletion(['zyx', 'wvu', 'tsr']) == 3

    # Note that the rows of strs are not necessarily in lexicographic order:
    #i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)
    assert minDeletion2(strs = ['xc','yb', 'za']) == 0
