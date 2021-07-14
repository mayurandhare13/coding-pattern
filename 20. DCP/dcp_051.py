import random

def randomize(deck):
    n = len(deck)

    for i in range(n-1, 0, -1):
        j = random.randrange(0, i+1)
        deck[i], deck[j] = deck[j], deck[i]


if __name__ == '__main__':
    deck = list(range(1, 53))
    randomize(deck)
    print(deck)
