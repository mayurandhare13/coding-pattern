from mmh3 import hash
from bitarray import bitarray

class BloomFilter:

    def __init__(self, size, hashCount):
        self.size = size
        self.bitarray = bitarray(size)
        self.bitarray.setall(0)
        self.hashCount = hashCount

    def add(self, item):
        for i in range(self.hashCount):
            index = hash(item, i) % self.size
            self.bitarray[index] = 1
        
        return self
    
    def check(self, item):
        for i in range(self.hashCount):
            index = hash(item, i) % self.size
            if self.bitarray[index] == 0:
                return False
        
        return True


if __name__ == '__main__':
    bloom = BloomFilter(20, 10)

    animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
               'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
               'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
    
    for animal in animals:
        bloom.add(animal)

    for animal in animals:
        if bloom.check(animal):
            print(f'{animal} is in bloom filter as expected')
        else:
            print(f'{animal} is not in bloom filter as expected')

    # Membership existence for not inserted animals
    # There could be false positives
    other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
                     'whale', 'shark', 'fish', 'turkey', 'duck', 'dove',
                     'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla',
                     'hawk' ]

    for other_animal in other_animals:
        if bloom.check(other_animal):
            print(f'{other_animal} is not in the bloom, but a false positive')
        else:
            print(f'{other_animal} is not in the bloom filter as expected')
