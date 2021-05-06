from heapq import heappush, heappop
import heapq

def merge(lists):
    res = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, listIndex, elementIndex = heappop(heap)
        res.append(val)

        if elementIndex + 1 < len(lists[listIndex]):
            nextTuple = (
                lists[listIndex][elementIndex + 1],
                listIndex,
                elementIndex + 1
            )

            heappush(heap, nextTuple)
    
    return res


if __name__ == '__main__':
    res = merge([[10, 15, 30], [12, 15, 20], [17, 20, 32]])
    print(res)

    # O(N*K log K) <-- K list
