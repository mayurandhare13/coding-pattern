def isPalindrome(s):
    return s == s[::-1]


def getNearestPalindrome(s):
    if isPalindrome(s):
        return s
    
    if s[0] == s[-1]:
        return s[0] + getNearestPalindrome(s[1:-1]) + s[-1]
    
    else:
        pal1 = s[0] + getNearestPalindrome(s[1:]) + s[0]
        pal2 = s[-1] + getNearestPalindrome(s[:-1]) + s[-1]

        if len(pal1) < len(pal2):
            return pal1
        
        elif len(pal1) > len(pal2):
            return pal2
        
        return pal1 if pal1 < pal2 else pal2


if __name__ == '__main__':
    assert getNearestPalindrome('race') == 'ecarace'
    assert getNearestPalindrome('google') == 'elgoogle'
