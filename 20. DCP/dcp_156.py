from math import sqrt
from sys import maxsize

def perfectSquares(n: int) -> int:
    squares = [ i**2 for i in range(int(sqrt(n)) + 1)]

    dp = [maxsize] * (n + 1)
    dp[0] = 0

    for i in range(1, n+1):
        for sq in squares:
            if i < sq:
                break
            
            dp[i] = min(dp[i], dp[i - sq] + 1)
    
    return dp[-1]


if __name__ == '__main__':
    assert perfectSquares(13) == 2
    assert perfectSquares(27) == 3
