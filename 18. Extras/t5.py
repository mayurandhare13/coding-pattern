from heapq import heappush, heappop

def routepairs(maxTravelDist, forwardRoutes: list, returnRouts: list):
    flen = len(forwardRoutes)
    rlen = len(returnRouts)

    minHeap = []

    for i in range(flen):
        for j in range(rlen):
            dist = forwardRoutes[i][1] + returnRouts[j][1]
            if dist <= maxTravelDist:
                diff = maxTravelDist - dist
                heappush(minHeap, (diff, [forwardRoutes[i][0],returnRouts[j][0]]))

    result = []
    minDiff = minHeap[0][0]
    while minHeap:
        diff, index = heappop(minHeap)
        if diff != minDiff:
            break
        result.append(index)
    
    print(result)


if __name__ == '__main__':
    maxTravelDist = 10000
    forwardRoutes = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
    returnRouts = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]

    routepairs(maxTravelDist, forwardRoutes, returnRouts)
