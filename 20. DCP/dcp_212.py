def columnId(num):
    code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = len(code)

    id = []
    while num > 0:
        letter = code[(num - 1) % base]
        id.append(letter)

        num = (num - 1) // base
    
    return ''.join(reversed(id))


if __name__ == '__main__':
    print(columnId(27)) # 26^1 +  1
    print(columnId(51)) # 26^1 + 25
    print(columnId(52)) # 26^1 + 26
