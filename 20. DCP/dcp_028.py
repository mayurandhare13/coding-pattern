def justify(words: list, width: int) -> list:
    result, currentList, numberOfLetters = [], [], 0

    for word in words:
        # len(currentList) -> consider single space for every word
        if len(word) + len(currentList) + numberOfLetters > width:

            # we use max. 1 because atleast one word would be there and to avoid modulo by 0
            size = max(1, len(currentList)-1)

            # add space in round robin fashion
            # from left -> right words
            for i in range(width - numberOfLetters):
                index = i % size
                currentList[index] += ' '
            
            result.append(''.join(currentList))
            currentList = []
            numberOfLetters = 0
        
        currentList.append(word)
        numberOfLetters += len(word)

    # last line is left justified    
    lastLine = ' '.join(currentList).ljust(width)
    result.append(lastLine)

    return result


if __name__ == '__main__':
    words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    assert justify(words, 16) == ['the  quick brown', 'fox  jumps  over', 'the lazy dog    ']
    
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    assert justify(words, 16) == ['This    is    an', 'example  of text', 'justification.  ']
    
    words = ["What","must","be","acknowledgment","shall","be"]
    assert justify(words, 16) == ['What   must   be', 'acknowledgment  ', 'shall be        ']

    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    assert justify(words, 20) == ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
