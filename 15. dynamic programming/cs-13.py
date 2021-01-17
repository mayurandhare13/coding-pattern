'''
Strings Interleaving

Give three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’. ‘p’ would be considered interleaving ‘m’ and ‘n’ if it contains ALL THE LETTERS from ‘m’ and ‘n’ and the order of letters is preserved too.

Input: m="abd", n="cef", p="abcdef"
Output: true
Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.
'''

def find_SI_helper(m, n, p, mIndex, nIndex, pIndex):
    mLen, nLen, pLen = len(m), len(n), len(p)

    if mIndex == mLen and nIndex == nLen and pIndex == pLen:
        return True

    # if pattern exhaust
    if pIndex == pLen:
        return False

    b1, b2 = False, False
    if mIndex < mLen and m[mIndex] == p[pIndex]:
        b1 = find_SI_helper(m, n, p, mIndex + 1, nIndex, pIndex + 1)
    
    if nIndex < nLen and n[nIndex] == p[pIndex]:
        b2 = find_SI_helper(m, n, p, mIndex, nIndex + 1, pIndex + 1)

    return b1 or b2


def find_SI(m, n, p):
    return find_SI_helper(m, n, p, 0, 0, 0)


if __name__ == "__main__":
    print(find_SI("abd", "cef", "abcdef"))
    print(find_SI("abd", "cef", "adcbef"))
    print(find_SI("abc", "def", "abdccf"))
    print(find_SI("abcdef", "mnop", "mnaobcdepf"))
