from collections import defaultdict

def groupAnagrams1(strs: list):
    charMap = defaultdict(list)

    # O(n)
    for s in strs:
        # O(klogk)
        key = sorted(s)
        charMap[tuple(key)].append(s)

    for k, v in charMap.items():
        print(f"{k} --> {v}")

    # O(n * klogk)


def groupAnagrams2(strs: list):
    charMap = defaultdict(list)

    # O(n)
    for s in strs:
        tmp = [0] * 26
        # O(k)
        for c in s:
            tmp[ord(c) - ord('a')] = 1

        charMap[tuple(tmp)].append(s)

    for v in charMap.values():
        print(v)

    # O(nk)





if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    groupAnagrams1(strs)

    print('-' * 20)
    groupAnagrams2(strs)
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

