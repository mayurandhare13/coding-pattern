class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = next(iterator)

    def peek(self):
        return self._next

    def next(self):
        result = self._next
        try:
            self._next = next(self.iterator)
        except StopIteration:
            self._next = None

        return result

    def hasNext(self):
        return self._next is not None


if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    iterator = iter(sample)
    peekable = PeekableInterface(iterator)

    assert peekable.peek() == 1
    assert peekable.hasNext()

    assert peekable.next() == 1
    assert peekable.next() == 2
    assert peekable.next() == 3
    assert peekable.next() == 4

    assert peekable.peek() == 5
    assert peekable.next() == 5

    assert peekable.peek() == None
    assert peekable.next() == None
