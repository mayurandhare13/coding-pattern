'''
Monte Carlo methods are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results.
More tests give more accurate result

area of circle               no. of points generated inside the circle
------------------   =   -------------------------------------------------
area of square              total no. of points generated (or in square)  


area of square is 1 sq. unit
x^2 + y^2 <= 1
'''

import random

def estimatePi(iterations) -> float:
    pi = 0.0
    circlePoints, squarePoints = 0, 0

    for i in range(iterations):
        # Randomly generated x and y values from a
        # uniform distribution Range of x and y values is -1 to 1

        randX = random.uniform(-1, 1)
        randY = random.uniform(-1, 1)

        originDistance = randX**2 + randY**2

        if originDistance <= 1:
            circlePoints += 1
        
        squarePoints += 1

    # pi= 4  *  (no. of points generated inside the circle) / 
    #           (no. of points generated inside the square)
    pi = 4 * circlePoints / squarePoints
    
    return pi


if __name__ == '__main__':
    print("{:1.3f}".format(estimatePi(1000000)))
    print(round(estimatePi(1000000), 3))

