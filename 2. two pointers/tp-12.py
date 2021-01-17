'''
Comparing Strings containing Backspaces (medium)
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal. O(M+N)

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
'''

def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 and index2 >= 0:
        i1 = get_next_valid_char_index(str1, index1)
        i2 = get_next_valid_char_index(str2, index2)
        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if str1[i1] != str2[i2]:
            return False
            
        index1 = i1 - 1
        index2 = i2 - 1
    
    return True


def get_next_valid_char_index(str, index):
    backspace_count = 0
    while index >= 0:
        if str[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break

        index -= 1
    
    return index


if __name__ == "__main__":
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("dxp#", "dxyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))
