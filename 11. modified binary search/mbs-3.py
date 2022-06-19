'''
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array "greater" than a given 'key'.

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
'''

def search_next_letter(letters, key):
    start, end = 0, len(letters) - 1
    if key < letters[start] or key > letters[end]:
        return letters[0]

    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return letters[start % len(letters)]


if __name__ == "__main__":
    print(search_next_letter(['a', 'c', 'f', 'h'], key = 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], key = 'm'))


# trick: if asked next big number than key --> return start
# because we increment the start and decrement the end
# applied vice-versa