def wordSearch(matrix: list[list], word: str) -> bool:
    
    rows = len(matrix)
    cols = len(matrix[0])
    wordLen = len(word)
    firstChar = word[0]

    for i in range(rows):
        row = matrix[i]
        if firstChar not in row:
            continue

        firstCharIndex = row.index(firstChar)

        # search horizontally
        if cols - firstCharIndex >= wordLen:
            possibleWord = row[firstCharIndex: firstCharIndex+wordLen]
            if ''.join(possibleWord) == word:
                return True

        # search vertically
        possibleWord = []
        if rows - i >= wordLen:
            for j in range(wordLen):
                possibleWord.append(matrix[i + j][firstCharIndex])
        
        if ''.join(possibleWord) == word:
            return True
    
    return False


if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
                ['O', 'B', 'Q', 'P'],
                ['A', 'N', 'O', 'B'],
                ['M', 'A', 'S', 'S']]
    
    assert wordSearch(matrix, 'FOAM') == True
    assert wordSearch(matrix, 'MASS') == True
