# Valid Credit Card Number

'''
1. Reverse Number
2. sum all odd index val --> S1
3. multiple even index val
    if val == 8
        8 * 2 = 16 then sum the integers --> 1 + 6 = 7
        v = 16 --> v // 10 + v % 10 == 1 + 6 = 7
4. Add Odd + Even
5. total sum should have 0 at the unit place. (total % 10 == 0)
'''


def isValidCard(number: str):
    numList = [int(c) for c in reversed(number) if c.isdigit()]

    oddSum = 0
    evenSum = 0

    for i, val in enumerate(numList):
        # odd index
        if i % 2 == 0:
            oddSum += val

        # even index
        else:
            v = (val * 2)
            evenSum += v // 10
            evenSum += v % 10
    
    total = oddSum + evenSum
    
    return total % 10 == 0


if __name__ == '__main__':
    print(isValidCard('49927398716'))
