# There at most will be 81 searches since there are 81 permutations (3^4) max for a given string that fits into an IP structure.

def validBlock(block: str) -> bool:

    if len(block) > 1 and block[0] == '0':
        return False
    
    if len(block) == 3 and int(block) > 255:
        return False

    return True


def restoreHelper(s, result, ip, count):
    if count == 4:
        if len(s) == 0:
            # remove last `.`
            result.append(ip[:-1])
        return
    
    for i in range(1, min(4, len(s)+1)):
        block = s[0:i]
        if validBlock(block):
            restoreHelper(s[i:], result, ip + block + '.', count + 1)


def restoreIpAddresses(s: str) -> list:
    result = []
    restoreHelper(s, result, '', 0)
    return result


if __name__ == '__main__':
    assert restoreIpAddresses('2542540123') == ['254.25.40.123', '254.254.0.123']
    # iterations = 78
    assert restoreIpAddresses('010010') == ['0.10.0.10', '0.100.1.0']
    # iterations = 20
    assert restoreIpAddresses('0000') == ['0.0.0.0']
    # iterations = 9
    assert restoreIpAddresses('1111') == ['1.1.1.1']
    # iterations = 14
    assert restoreIpAddresses('101023') == ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']
    # iterations = 33
