'''
Employee Free Time (hard)
For 'K' employees, we are given a list of intervals representing the working hours of each employee. Our goal is to find out if there is a free interval that is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employess are free between [4,6] and [8,9].
'''

from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval    # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex    # index of the interval in the employee list

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    minHeap, result = [], []
    n = len(schedule)
    
    # insert first interval of each employee to the queue
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    prevInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        
        # if prevInterval is not overlapping with next interval, then insert free interval
        if prevInterval.end < queueTop.interval.start:
            result.append(Interval(prevInterval.end, 
                                    queueTop.interval.start))
            prevInterval = queueTop.interval
        
        # overlapping intervals, update the previousInterval if needed
        elif prevInterval.end < queueTop.interval.end:
            prevInterval = queueTop.interval

        # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(
                                employeeSchedule[queueTop.intervalIndex + 1],
                                queueTop.employeeIndex,
                                queueTop.intervalIndex + 1
                            )
            )

    return result


if __name__ == "__main__":

    input = [[Interval(1, 3), Interval(5, 6)],
            [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], 
            [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [Interval(2, 4)], 
            [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()




'''
Simple Solution
Put the working hours of all employees in a list and sort them on the start time. Then we can iterate through the list to find the gaps.

Better Solution
Since we have both lists which are sorted.
'''