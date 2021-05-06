def throwDice(N, faces, total):
    def dp(N, faces, total):
        if N == 0:
            return total == 0

        if total < 0 or total < N or N * faces < total:
            return 0

        if lookup[N][total] == 0:
            for i in range(1, faces + 1):
                lookup[N][total] += dp(N - 1, faces, total - i)
        
        return lookup[N][total]
    
    lookup = [[0 for x in range(total + 1)] for i in range(N + 1)]
    return dp(N, faces, total)


if __name__ == '__main__':
    print(throwDice(3, 6, 7))
    print(throwDice(4, 6, 15))
