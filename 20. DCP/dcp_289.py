# Source: https://en.wikipedia.org/wiki/Nim#Mathematical_theory

'''
A B C nim-sum 
 
3 4 5 0102=210   I take 2 from A, leaving a sum of 000, so I will win.
1 4 5 0002=010   You take 2 from C
1 4 3 1102=610   I take 2 from B
1 2 3 0002=010   You take 1 from C
1 2 2 0012=110   I take 1 from A
0 2 2 0002=010   You take 1 from C
0 2 1 0112=310   The normal play strategy would be to take 1 from B, leaving an even number (2)
                 heaps of size 1.  For misère play, I take the entire B heap, to leave an odd
                 number (1) of heaps of size 1.
0 0 1 0012=110   You take 1 from C, and lose.
'''

import functools

def has_forced_win(heaps):
    
    nimSum = functools.reduce(lambda x, y: x ^ y, heaps)
    
    if nimSum == 0:
        return False

    for heap in heaps:
        xa = heap ^ nimSum
        if xa < heap:
            return True

    return False


if __name__ == "__main__":
    print(has_forced_win([1, 2, 3]))
    print(has_forced_win([1, 2, 4]))
    print(has_forced_win([3, 4, 5]))
