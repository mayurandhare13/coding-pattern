class Iterator:
    def __init__(self, lsts):
        self._lsts = lsts
        self.i = None
        self.j = None


    def _nextCoords(self, i, j):
        # get coordinates of next valid element
        if not self._lsts or len(self._lsts) == 0:
            return None

        if i is None and j is None:
            i = 0
            while i < len(self._lsts):
                if len(self._lsts[i]) > 0:
                    return (i, 0)
                i += 1

        if j + 1 < len(self._lsts[i]):
            return (i, j + 1)

        i += 1
        while i < len(self._lsts):
            if len(self._lsts[i]) > 0:
                return (i, 0)
            i += 1

        return None


    def next(self):
        coords = self._nextCoords(self.i, self.j)
        if coords is None:
            raise Exception('No more elements')

        else:
            self.i, self.j = coords
            return self._lsts[self.i][self.j]


    def hasNext(self):
        coords = self._nextCoords(self.i, self.j)
        return coords is not None



if __name__ == '__main__':
    i = Iterator([[1, 2], [3], [], [4, 5, 6]])
    assert i.next() == 1
    assert i.next() == 2
    assert i.next() == 3
    assert i.next() == 4
    assert i.next() == 5
    assert i.hasNext() == True
    assert i.next() == 6
    assert i.hasNext() == False
