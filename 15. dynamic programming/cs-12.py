'''
Edit Distance

Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters.
(refer cs-11 & cs-3 for minimum deletion and insertion)

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: We can replace first 'a' with 'c' and delete second 'c'.
'''

def find_min_operations_helper(str1, str2, index1, index2):
    n1, n2 = len(str1), len(str2)

    # if we have reached the end of s1, then we have to insert all the remaining characters of s2
    if index1 == n1:
        return n2 - index2

    # if we have reached the end of s2, then we have to delete all the remaining characters of s1
    if index2 == n2:
        return n1 - index1
    
    # If the strings have a matching character, we can recursively match for the remaining lengths
    if str1[index1] == str2[index2]:
        return find_min_operations_helper(str1, str2, index1 + 1, index2 + 1)
    
    # deletion in s1
    c1 = 1 + find_min_operations_helper(str1, str2, index1 + 1, index2)

    # insertion in s1
    c2 = 1 + find_min_operations_helper(str1, str2, index1, index2 + 1)

    # replace in s1
    c3 = 1 + find_min_operations_helper(str1, str2, index1 + 1, index2 + 1)

    return min(c1, c2, c3)


def find_min_operations(str1, str2):
    return find_min_operations_helper(str1, str2, 0, 0)


def find_min_operations2(str1, str2):
    l1, l2 = len(str1), len(str2)
    memo = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    
    #str1 is empty
    for j in range(l2+1):
        memo[0][j] = j
    
    # str2 is empty
    for i in range(l1+1):
        memo[i][0] = i

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = min(memo[i-1][j-1], memo[i][j-1], memo[i-1][j]) + 1
    
    return memo[l1][l2]


if __name__ == "__main__":
    print(find_min_operations("bat", "but"))
    print(find_min_operations("abdca", "cbda"))
    print(find_min_operations("passpot", "ppsspqrt"))
    print(find_min_operations2("passpot", "ppsspqrt"))
    print(find_min_operations2("", "ppsspqrt"))
