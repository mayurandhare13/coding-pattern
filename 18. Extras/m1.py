'''
Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.
'''

from collections import Counter

def isvalid(s: str):
    counts = Counter(s)
    return len([c for c, f in counts.items() if (f % 2 == 1)]) <= 1


def minswaps(s: str):
    if not isvalid(s):
        return -1
    
    s = list(s)
    swaps = 0
    f, b = 0, len(s) - 1

    while f < b:
        # FRONT == BACK
        if s[f] == s[b]:
            f += 1
            b -= 1
        
        else:
            # FIND RIGHTMOST CHAR TO MATCH FRONT
            mid = b
            while mid > f and s[mid] != s[f]:
                mid -= 1
            
            # CHAR NOT FOUND
            if f == mid:
                s[mid], s[mid+1] = s[mid+1], s[mid]
                swaps += 1
                continue

            # CHAR FOUND. SWAP TILL FUND CORRECT POSITION `b`
            for i in range(mid, b):
                s[i], s[i+1] = s[i+1], s[i]
                swaps += 1
            
            # SHRINK WINDOW
            f += 1
            b -= 1
    
    return swaps


if __name__ == '__main__':
    assert minswaps('mamad') == 3
    assert minswaps('asflkj') == -1
    assert minswaps('aabb') == 2
