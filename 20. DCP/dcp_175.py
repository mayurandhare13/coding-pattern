from collections import defaultdict
from random import random


def transform(transProb):
    d = defaultdict(dict)

    for start, end, prob in transProb:
        d[start][end] = prob

    return d


def nextState(current, transDict: dict[dict]):
    r = random()
    for state, p in transDict[current].items():
        r -= p
        if r <= 0:
            return state


def histogramCounts(start, transProbs, numSteps):
    transDict = transform(transProbs)
    countHistogram = defaultdict(int)

    current = start
    for i in range(numSteps):
        countHistogram[current] += 1
        nextStateVal = nextState(current, transDict)
        current = nextStateVal

    return countHistogram


if __name__ == '__main__':
    markovProbs = [
                    ('a', 'a', 0.9),
                    ('a', 'b', 0.075),
                    ('a', 'c', 0.025),
                    ('b', 'a', 0.15),
                    ('b', 'b', 0.8),
                    ('b', 'c', 0.05),
                    ('c', 'a', 0.25),
                    ('c', 'b', 0.25),
                    ('c', 'c', 0.5)
                ]
    histogram = histogramCounts('a', markovProbs, 5000)
    print(histogram)    # {'a': 3148, 'c': 333, 'b': 1519}
