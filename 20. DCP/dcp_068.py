def printBoard(M, bishops):
    board = [['0' for _ in range(M)] for _ in range(M)]

    for b in bishops:
        r, c = b[0], b[1]
        board[r][c] = 'b'
    
    for row in board:
        print(row)

    print('-' * 30)


def bishopAttack(M, bishops):
    printBoard(M, bishops)

    attacks = 0

    for i in range(len(bishops) - 1):
        for j in range(i+1, len(bishops)):
            b1 = bishops[i]
            b2 = bishops[j]

            if abs(b1[0] - b2[0]) == abs(b1[1] - b2[1]):
                attacks += 1
    
    return attacks


if __name__ == '__main__':
    assert bishopAttack(5, [(0, 0), (1, 2), (2, 2), (4, 0)]) == 2
    assert bishopAttack(5, [(0, 4), (1, 2), (2, 2), (4, 0)]) == 3
