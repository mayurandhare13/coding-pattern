'''
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
'''

def solve(sentence, k):
    words = sentence.split()

    brokenText = []
    bufferArr = []
    
    # for every word need one space.
    # last word may / may not have space
    bufferLen = -1
    idx = 0

    while idx < len(words):
        word = words[idx]

        if len(word) > k:
            return None
        
        if len(word) + 1 + bufferLen <= k:
            bufferLen += len(word) + 1
            bufferArr.append(word)
            idx += 1
        else:
            brokenText.append(' '.join(bufferArr))
            bufferArr = []
            bufferLen = -1
    
    if bufferArr:
        brokenText.extend(bufferArr)
    
    return brokenText


if __name__ == '__main__':
    sentence = 'the quick brown fox jumps over the lazy dog'
    res = solve(sentence, 10)
    print(res)
