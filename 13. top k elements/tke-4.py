'''
Connect Ropes (easy)

Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.

Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

Given ‘N’ ropes, we need O(N∗logN) to insert all the ropes in the heap.
'''

from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
    minHeap = []
    # add all ropes to the min heap
    for i in ropeLengths:
        heappush(minHeap, i)
    
    # go through the values of heap. In each step take top (lowest) rope length from meanHeap
    # connect them and push back to the min heap
    result, temp = 0, 0
    while len(minHeap) > 1:
        temp = heappop(minHeap) + heappop(minHeap)
        result += temp
        heappush(minHeap, temp)
    
    return result


if __name__ == "__main__":
    print(minimum_cost_to_connect_ropes([1, 3, 11, 5]))
    print(minimum_cost_to_connect_ropes([3, 4, 5, 6]))
    print(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]))
