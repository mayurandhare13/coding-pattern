'''
Minimum Deletions & Insertions to Transform a String into another

Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. 

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2 deletions and 1 insertion.
Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

1. To transform s1 into s2, we need to delete everything from s1 which is not part of LCS, so minimum deletions we need to perform from s1 => len1 - LCS
2. we need to insert everything in s1 which is present in s2 but not part of LCS, so minimum insertions we need to perform in s1 => len2 - LCS
'''

def find_MDI_helper(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0

    if s1[index1] == s2[index2]:
        return 1 + find_MDI_helper(s1, s2, index1 + 1, index2 + 1)
    
    c1 = find_MDI_helper(s1, s2, index1 + 1, index2)
    c2 = find_MDI_helper(s1, s2, index1, index2 + 1)

    return max(c1, c2)


def find_MDI(s1, s2):
    lcs = find_MDI_helper(s1, s2, 0, 0)
    print(f"total deletion from s1({s1}): {len(s1) - lcs}")
    print(f"total insertion from s2({s2}): {len(s2) - lcs}")
    print("shorted Super-Sequence total: ", len(s1) + len(s2) - lcs, '\n')


if __name__ == "__main__":
    find_MDI("abdca", "cbda")
    find_MDI("abc", "fbc")
    find_MDI("passport", "ppsspt")
    find_MDI("abcf", "bdcf")
    find_MDI("dynamic", "programming")
