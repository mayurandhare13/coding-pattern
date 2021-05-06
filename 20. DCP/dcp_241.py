def getHIndex(citations: list):
    citations.sort(reverse=True)
    
    for i, citCount in  enumerate(citations):
        if i >= citCount:
            return i


if __name__ == '__main__':
    print(getHIndex([4, 3, 0, 1, 5]))
    print(getHIndex([3, 0, 6, 1, 5]))
