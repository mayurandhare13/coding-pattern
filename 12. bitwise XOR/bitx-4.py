'''
Complement of Base 10 Number (medium)

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.
'''


def calc_bitwise_complement(num):
    # calc total number of bits in `num`
    bit_count, n = 0, num
    while n > 0:
        bit_count += 1
        n = n >> 1
    
    # ‘8’ which is a complete power of ‘2’, { `1000` - `1` = `111` }
    # ‘7’ (one less than 8) has a binary representation of ‘111’ i.e., it has ‘3’ least significant bits set to ‘1’.
    
    all_bits_set = pow(2, bit_count) - 1

    return num ^ all_bits_set


if __name__ == "__main__":
    print(calc_bitwise_complement(8))
    print(calc_bitwise_complement(10))  # 1010, all_bits_set = 1000 - 1 = 111
                                        # 1010 ^ 111 = 101
