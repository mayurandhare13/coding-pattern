# https://github.com/ranzhang/blockchain/tree/master/crypto/hashing?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com

from hashlib import sha256
import json
from collections import OrderedDict


class MerkTree:
    def __init__(self, transactions: list):
        self.transactions = transactions
        self.transactionsMap = OrderedDict()


    def buildTree(self, hash=[]):
        hash = self.transactions if len(hash) == 0 else hash
        if len(hash) % 2 != 0:
            hash.extend(hash[-1:])

        hash2 = []

        for i in range(0, len(hash), 2):
            h1 = sha256(hash[i].encode())
            self.transactionsMap[hash[i]] = h1.hexdigest()

            h2 = sha256(hash[i+1].encode())
            self.transactionsMap[hash[i+1]] = h2.hexdigest()

            hash2.append(h1.hexdigest() + h2.hexdigest())

        if len(hash2) != 1:
            self.buildTree(hash2)

    
    def getTransactionsMap(self):
        return self.transactionsMap


    def getRoot(self):
        lastKey = list(self.transactionsMap.keys())[-1]
        return self.transactionsMap[lastKey]


if __name__ == '__main__':
    mt = MerkTree(['a', 'b', 'c', 'd', 'e'])
    mt.buildTree()

    print('Final root of the tree : ', mt.getRoot())

    transMap = mt.getTransactionsMap()
    print(json.dumps(transMap, indent=4))
    print ('-' * 50)
