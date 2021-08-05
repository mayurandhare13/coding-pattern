import math

BITS_PER_INT = 32

class BitArray():
    def __init__(self, size) -> None:
        self._list = [0] * math.ceil(size / BITS_PER_INT)
        self._size = size
    

    def _boundsCheck(self, i):
        if i < 0 or i > self._size:
            raise IndexError('Index out of bounds')


    def get(self, i):
        self._boundsCheck(i)

        listIndex = i // BITS_PER_INT
        elementIndex = i % BITS_PER_INT

        return (self._list[listIndex] >> elementIndex) & 1
    

    def set(self, i, val):
        self._boundsCheck(i)

        listIndex = i // BITS_PER_INT
        elementIndex = i % BITS_PER_INT

        # -1 = ~1 + 1 == 1111 1111 1111 1111
        self._list[listIndex] = \
            self._list[listIndex] ^ (-val ^ self._list[listIndex]) & (1 << elementIndex)


    def __str__(self):
        return f"{[self.get(i) for i in range(self._size)]}"


if __name__ == '__main__':
    ba = BitArray(10)

    ba.set(0, 1)

    ba.set(3, 1)
    assert ba.get(3) == 1

    ba.set(6, 1)
    assert ba.get(6) == 1

    ba.set(8, 1)
    assert ba.get(8) == 1

    ba.set(3, 0)
    ba.get(3) == 0

    print(ba) # [1, 0, 0, 0, 0, 0, 1, 0, 1, 0]
