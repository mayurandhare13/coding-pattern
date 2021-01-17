'''
Unique Generalized Abbreviations (hard)

Given a word, write a function to generate all of its unique generalized abbreviations.

Input: "BAT"
Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"
'''

from collections import deque

class AbbreviatedWord:
    def __init__(self, str: list, start: int, count: int):
        self.str = str
        self.start = start
        self.count = count


def generate_generalized_abbreviation(word):
    result = []
    wordLen = len(word)
    queue = deque()
    queue.append(AbbreviatedWord(list(), 0, 0))

    while queue:
        abWord = queue.popleft()
        if abWord.start == wordLen:
            if abWord.count != 0:
                abWord.str.append(str(abWord.count))
            result.append(''.join(abWord.str))
        else:
            # continue abbreviating by incrementing the current abbreviation count
            queue.append(AbbreviatedWord(list(abWord.str), abWord.start + 1, abWord.count + 1))

            # restart abbreviating, append the count and the current character to the string
            if abWord.count != 0:
                abWord.str.append(str(abWord.count))
            
            newWord = list(abWord.str)
            newWord.append(word[abWord.start])
            queue.append(AbbreviatedWord(newWord, abWord.start + 1, 0))

    return result


if __name__ == "__main__":
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))
