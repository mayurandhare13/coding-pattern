def zigzag(s: str, nRows: int) -> str:
    l = len(s)
    arr = ['' for _ in range(nRows)]

    row = 0
    direction = -1

    for i in range(l):
        for r in range(nRows):
            if r == row:
                arr[r] += s[i]
            else:
                arr[r] += ' '
        
        if row == nRows - 1 or row == 0:
            direction *= -1
        
        row += direction
    
    return '\n'.join(arr)


if __name__ == '__main__':

    s = "123456789ABCDEFGHIJKL"\
		"MNOPQRSTUVWXYZabcdefghi"\
		"jklmnopqrstuvwxyz"
    rows = 9

    print(zigzag(s, rows))

    """
1               H               X               n            
 2             G I             W Y             m o           
  3           F   J           V   Z           l   p          
   4         E     K         U     a         k     q         
    5       D       L       T       b       j       r       z
     6     C         M     S         c     i         s     y 
      7   B           N   R           d   h           t   x  
       8 A             O Q             e g             u w   
        9               P               f               v    
    """

    print(zigzag('thisisazigzag', 4))
"""
t     a     g
 h   s z   a 
  i i   i z  
   s     g   
"""