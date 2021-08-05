class SparseArray:
    def __init__(self, arr, n):
        self.n = n
        self._dict = {}

        for i, val in enumerate(arr):
            if val != 0:
                self._dict[i] = val
    

    def _checkBounds(self, idx):
        if idx < 0 or idx >= self.n:
            raise IndexError('Out of bounds')


    def get(self, i):
        self._checkBounds(i)
        return self._dict.get(i, 0)
    

    def set(self, i, val):
        self._checkBounds(i)
        if val != 0:
            self._dict[i] = val
            return
        
        # if val = 0 then delete entry
        elif i in self._dict:
            del self._dict[i]


if __name__ == '__main__':
    arr = [1, 0, 0, 0, 3, 0, 2]

    sa = SparseArray(arr, len(arr))

    assert sa._dict == {0: 1, 4: 3, 6: 2}

    sa.set(2, 4)
    assert sa.get(2) == 4
    sa.set(4, 1)
    assert sa.get(4) == 1
    sa.set(0, 0)
    assert not sa.get(0)
