from heapq import *

class Lecture:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.end < other.end


def getMinRooms(lectures: list[Lecture]) -> int:
    lectures.sort(key=lambda x : x.start)

    minHeap = []
    minRooms = 0

    for lecture in lectures:
        while minHeap and lecture.start >= minHeap[0].end:
            heappop(minHeap)

        heappush(minHeap, lecture)
        minRooms = max(minRooms, len(minHeap))

    return minRooms


if __name__ == '__main__':
    assert getMinRooms([Lecture(30, 75), Lecture(0, 50), Lecture(60, 150)]) == 2
    assert getMinRooms([Lecture(6, 7), Lecture(2, 4), Lecture(8, 12)]) == 1
