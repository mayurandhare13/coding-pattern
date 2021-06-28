"""
both zigzag string is same
    P     I    N
    A   L S  I G    
    Y A   H R
    P     I

    P     I    N
        A   L S  I G
        Y A   H R
        P     I
"""

def printZigzagConcat(string, n) -> str:
    if n == 1:
        return string
    
    l = len(string)
    arr = ['' for _ in range(n)]
    row = 0

    for i in range(l):
        arr[row] += string[i]
        
        if row == 0:
            down = True

        elif row == n-1:
            down = False
        
        if down:
            row += 1
        else:
            row -= 1

    return ''.join(arr)


def convert(string, nRows) -> str:
    l = len(string)
    arr = ['' for _ in range(nRows)]

    i = 0
    while i < l:
        for r in range(nRows):      # vertically down / oblically down
            if i >= l:
                break
            arr[r] += string[i]
            i += 1
        
        for r in range(nRows-2, 0, -1): # oblically up
            if i >= l:
                break
            arr[r] += string[i]
            i += 1
    
    return ''.join(arr)


def convert2(string, nRows):
    if nRows == 1:
        return string
    
    l = len(string)
    arr = ['' for _ in range(nRows)]
    cycleLen = 2*nRows - 2

    for i in range(nRows):
        for j in range(i, l, cycleLen):
            arr[i] += string[j]

            # for 2nd element go to next cycle index and back by 2 times row index
            k = j + cycleLen - 2*i
            if i != 0 and i != nRows-1 and k < l:
                arr[i] += string[k]
    
    return ''.join(arr)


if __name__ == '__main__':
    assert printZigzagConcat('GEEKSFORGEEKS', 3) == 'GSGSEKFREKEOE'
    assert convert('GEEKSFORGEEKS', 3) == 'GSGSEKFREKEOE'
    assert convert2('GEEKSFORGEEKS', 3) == 'GSGSEKFREKEOE'
    
    assert printZigzagConcat('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert convert2('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
