'''
Longest Repeating Subsequence

Input: “t o m o r r o w”
Output: 2
Explanation: The longest repeating subsequence is “or” {tomorrow}.

Input: “f m f f”
Output: 2
Explanation: The longest repeating subsequence is “f f” {f m f, m f f}. Please note the second last character is shared in LRS.
'''

def find_LRS_length_helper(str, index1, index2):
    if index1 == len(str) or index2 == len(str):
        return 0

    if index1 != index2 and str[index1] == str[index2]:
        return 1 + find_LRS_length_helper(str, index1 + 1, index2 + 1)

    c1 = find_LRS_length_helper(str, index1 + 1, index2)
    c2 = find_LRS_length_helper(str, index1, index2 + 1)

    return max(c1, c2)


def find_LRS_length(str):
    return find_LRS_length_helper(str, 0, 0)


if __name__ == "__main__":
    print(find_LRS_length("tomorrow"))
    print(find_LRS_length("fmff"))
    print(find_LRS_length("aabdbcec"))
