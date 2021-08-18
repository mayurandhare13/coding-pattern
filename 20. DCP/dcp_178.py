from random import randint

NUM_OF_TRIALS = 1000

def d6():
    return randint(1, 6)


def gameOne():
    prev, curr = None, None
    cost = 0
    while prev != 5 and curr != 6:
        prev = curr
        curr = d6()
        cost += 1
    
    return cost


def gameTwo():
    prev, curr = None, None
    cost = 0
    while prev != 5 and curr != 5:
        prev = curr
        curr = d6()
        cost += 1
    
    return cost


def evalGames():
    game1, game2 = [], []
    for _ in range(NUM_OF_TRIALS):
        game1.append(gameOne())
        game2.append(gameTwo())
    
    print(f"Game 1: {sum(game1) / NUM_OF_TRIALS}")
    print(f"Game 2: {sum(game2) / NUM_OF_TRIALS}")


evalGames()
