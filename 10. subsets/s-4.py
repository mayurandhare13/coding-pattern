'''
String Permutations by changing case (medium)
Given a string, find all of its permutations preserving the character sequence but changing case.

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 
'''


def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)

    for i in range(len(str)):
        if str[i].isalpha():
            # we will take all existing permutations and change the letter case appropriately
            n = len(permutations)
            for p in range(n):
                chs = list(permutations[p])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations


if __name__ == "__main__":
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))
