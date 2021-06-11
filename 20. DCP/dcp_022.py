def sentence_break_helper(s: str, words: set, start: int):
    if start == len(s):
        return []

    sentence_words = list()
    for i in range(start+1, len(s)+1):
        word = s[start : i]
        if word in words:
            sentence_words.append(word)
            sentence_words.extend(sentence_break_helper(s, words, i))
            break
    
    return sentence_words


def sentence_break(s: str, words: list) -> list:
    return sentence_break_helper(s, set(words), 0)


if __name__ == '__main__':
    print (
        sentence_break('bedbathandbeyond', 
                    ['bed', 'bath', 'bedbath', 'and', 'beyond']
                )
    )

    print (
        sentence_break(
            'thequickbrownfox',
            ['quick', 'brown', 'the', 'fox']
        )
    )


