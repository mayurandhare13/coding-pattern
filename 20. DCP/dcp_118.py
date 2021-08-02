def square(lst: list) -> list:
    i, j = 0, len(lst) - 1

    output = [0] * len(lst)
    k = len(lst) - 1

    while i <= j:
        iSquare = lst[i] * lst[i]
        jSquare = lst[j] * lst[j]

        if iSquare > jSquare:
            output[k] = iSquare
            i += 1
        else:
            output[k] = jSquare
            j -= 1

        k -= 1

    return output
        


if __name__ == '__main__':
    assert square([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
