from collections import defaultdict


def findWordConcatenation(str, words: list):
    wordFrequency = defaultdict(int)

    for word in words:
        wordFrequency[word] += 1

    result = []
    count = len(words)
    wordLen = len(words[0])

    for i in range((len(str) - count * wordLen) + 1):
        seen = defaultdict(int)

        for j in range(count):
            nextWord = i + j * wordLen
            word = str[nextWord : nextWord + wordLen]

            if word not in wordFrequency:
                break

            seen[word] += 1

            if seen[word] > wordFrequency[word]:
                break

            if j + 1 == count:
                result.append(i)

    return result


if __name__ == '__main__':
    assert findWordConcatenation('dogcatcatcodecatdog', ['cat', 'dog']) == [0, 13]
    assert findWordConcatenation('barfoobazbitbyte', ['cat', 'dog']) == []
