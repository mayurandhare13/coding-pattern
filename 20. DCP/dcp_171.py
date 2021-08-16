import random
import time


def movementType():
    if random.random() > 0.5:
        return 'enter'
    else:
        return 'exit'


def busiest(movements: list):
    movements.sort(key=lambda x: x['timestamp'])
    inside = 0
    maxInside = 0

    start, end = 0, 0

    for m in movements:
        if m['type'] == 'enter':
            inside += m['count']
        
        elif m['type'] == 'exit':
            inside -= m['count']
        
        if inside < 0:
            inside = 0

        if inside > maxInside:
            maxInside = inside
            start = m['timestamp']
    

    for m in movements:
        if m['timestamp'] > start and m['type'] == 'exit':
            end = m['timestamp']
            break
    
    return (start, end)


if __name__ == '__main__':
    end = round(time.time())
    start = end - 86400

    movements = [
        {
            'timestamp' : random.randint(start, end),
            'count' : random.randint(1, 5),
            'type' : movementType()
        } for i in range(50)
    ]

    print (busiest(movements))
