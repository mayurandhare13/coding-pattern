'''
Minimum Deletions in a String to make it a Palindrome

Input: "abdbca"
Output: 1
Explanation: By removing "c", we get a palindrome "abdba".
'''

def find_minimum_deletion_helper(str, start, end):
    if start > end:
        return 0
    
    if start == end:
        return 1

    if str[start] == str[end]:
        return 2 + find_minimum_deletion_helper(
                    str, start + 1, end - 1
                )
    
    c1 = find_minimum_deletion_helper(str, start + 1, end)
    c2 = find_minimum_deletion_helper(str, start, end - 1)
    return max(c1, c2)


def find_minimum_deletion(str):
    n = len(str)
    return n - find_minimum_deletion_helper(str, 0, n - 1)


if __name__ == "__main__":
    print(find_minimum_deletion("abdbca"))
    print(find_minimum_deletion("cddpd"))
    print(find_minimum_deletion("pqr"))
