'''
Shortest Common Super-sequence

(also refer cs-3)
Input: s1: "abcf" s2:"bdcf" 
Output: 5
Explanation: The shortest common super-sequence (SCS) is "abdcf". 
'''

def find_SCS_length_helper(str1, str2, index1, index2):
    n1, n2 = len(str1), len(str2)
    
    # if we reach to end of str1, then we have to add remaining chars from str2
    if index1 == n1:
        return n2 - index2

    if index2 == n2:
        return n1 - index1

    if str1[index1] == str2[index2]:
        return 1 + find_SCS_length_helper(str1, str2, index1 + 1, index2 + 1)
    
    # skips(deletes) element from String-1
    c1 = 1 + find_SCS_length_helper(str1, str2, index1 + 1, index2)
    
    # insert element from String-2
    c2 = 1 + find_SCS_length_helper(str1, str2, index1, index2 + 1)

    return min(c1, c2)

def find_SCS_length(str1, str2):
    return find_SCS_length_helper(str1, str2, 0, 0)


if __name__ == "__main__":
    print(find_SCS_length("abcf", "bdcf"))
    print(find_SCS_length("dynamic", "programming"))
