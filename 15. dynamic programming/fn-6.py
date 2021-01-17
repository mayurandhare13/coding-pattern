'''
House thief

There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses. The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system. How should the thief maximize his stealing?

Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4
'''

def find_max_steal_helper(wealth, index):
    if index >= len(wealth):
        return 0

    # steal from current house
    steal_current = wealth[index] + \
                        find_max_steal_helper(wealth, index + 2)
    
    # skip current
    skip_current = find_max_steal_helper(wealth, index + 1)

    return max(steal_current, skip_current)


def find_max_steal(wealth):
    return find_max_steal_helper(wealth, 0)


if __name__ == "__main__":
    print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal([2, 10, 14, 8, 1]))
