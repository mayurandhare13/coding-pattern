'''
Given a set with distinct elements, find all of its distinct subsets.
Input: [1, 3]
Output: [], [1], [3], [1,3]

To generate all subsets of the given set, we can use the Breadth First Search (BFS) approach.
'''


def find_subsets(nums):
    subsets = []
    
    # add empty set
    subsets.append([])

    for num in nums:
        # we will take all existing subsets and insert the current number in them to create new subsets
        # same as BFS | go level by level down
        _len = len(subsets)
        for i in range(_len):
            _set = list(subsets[i]) 
            # this is copy | if you don't use `list` then it will point to the same list and override/add element
            _set.append(num)
            subsets.append(_set)

    return subsets


if __name__ == "__main__":

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))



'''
In each step, the number of subsets doubles as we add each element to all the existing subsets, the time complexity of the above algorithm is O(2^N), where `N` is the total number of elements in the input set. This also means that, in the end, we will have a total of O(2^N) subsets.
'''