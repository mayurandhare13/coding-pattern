from collections import Counter


def isPermutationPalindrome2(s: str) -> bool:
    c = Counter(s)
    odds = 0
    for _, count in c.items():
        if count % 2 == 1:
            odds += 1
    
    return odds <= 1


def isPermutationPalindrome(s: str) -> bool:
    # constant memory
    arr = [0] * (128)
    odds = 0

    for c in s:
        i = ord(c)
        arr[i] += 1

        if arr[i] % 2 == 1:
            odds += 1
        else:
            odds -= 1
    
    return odds <= 1


if __name__ == '__main__':
    assert isPermutationPalindrome('carrace')
    assert not isPermutationPalindrome('daily')
