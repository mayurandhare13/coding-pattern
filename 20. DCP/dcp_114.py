import re

def reverse(string, delimiters):
    words = re.split('[' + delimiters + ']+', string)
    if len(words) > 1 and words[-1] == '':
        words = words[:-1]
    
    wordsIterator = reversed(words)

    output = []
    delimiterFound = True

    for c in string:
        if c in delimiters:
            output.append(c)
            delimiterFound = True
        else:
            if delimiterFound:
                try:
                    output.append(next(wordsIterator))
                except StopIteration:
                    pass
            delimiterFound = False

    return ''.join(output)


if __name__ == '__main__':
    assert reverse('hello/world:here/', ':/') == 'here/world:hello/'
    assert reverse('hello/world:here', ':/') == 'here/world:hello'
    assert reverse('hello//world:here', ':/') == 'here//world:hello'
