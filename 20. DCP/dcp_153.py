def minDistance(text, w1, w2):
    textWords = [ w.strip() for w in text.split(' ')]

    w1Index = [i for i, v in enumerate(textWords) if v == w1]
    w2Index = [i for i, v in enumerate(textWords) if v == w2]

    if not w1Index or not w2Index:
        return -1

    i = j = 0
    miniDistance = abs(w1Index[i] - w2Index[j])

    while i < len(w1Index) and j < len(w2Index):
        dist = abs(w1Index[i] - w2Index[j])
        miniDistance = min(miniDistance, dist)

        if w1Index[i] < w2Index[j]:
            i += 1

        else:
            j += 1

    return miniDistance - 1


if __name__ == '__main__':
    assert minDistance("dog cat hello cat dog dog hello cat world", 'hello', 'world') == 1
