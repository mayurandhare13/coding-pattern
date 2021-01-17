'''
Reconstructing a Sequence (hard) #
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.

Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
Output: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct 
[3, 1, 4, 2, 5].
'''

'''
HINT
We must perform the topological sort for the graph to determine two things:
1. Can the topological ordering construct the originalSeq?
2. That there is only one topological ordering of the numbers possible. 
This can be confirmed if we do not have more than one source at any time while finding the topological ordering of numbers.
'''

from collections import deque

def can_reconstruct(originalSeq: list, sequences: list) -> bool:
    if len(originalSeq) <= 0:
        return False

    # 1. initialize indegrees and graph
    indegrees = {}
    graph = {}
    for seq in sequences:
        for num in seq:
            indegrees[num] = 0
            graph[num] = []
    
    # 2. build graph
    for seq in sequences:
        for i in range(0, len(seq) - 1):
            parent, child = seq[i], seq[i+1]
            graph[parent].append(child)
            indegrees[child] += 1
    
    # if we don't have ordering rules for all numbers
    # we will not be able to reconstruct the original sequence
    if len(indegrees) != len(originalSeq):
        return False
    
    # 3. find all sources
    sources = deque()
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)
    
    # 4. sort | we should not have more than 1 source vertices
    # otherwise multiple sequences can be reconstructed
    sortedOrder = []
    while sources:
        if len(sources) > 1:
            return False
        
        # next source number != original sequence number
        if originalSeq[len(sortedOrder)] != sources[0]:
            return False
        
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sources.append(child)
    
    return len(sortedOrder) == len(originalSeq)


if __name__ == "__main__":
    print(can_reconstruct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]]))
    print(can_reconstruct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))
    print(can_reconstruct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]]))
    