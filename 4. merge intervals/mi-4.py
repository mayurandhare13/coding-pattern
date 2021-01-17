'''
Conflicting Appointments (medium)
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
'''


def can_attend_all_appointments(intervals):
    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])
    
    for i in range(1, len(intervals)):
        if intervals[i-1][end] > intervals[i][start]:
            return False

    return True


if __name__ == "__main__":
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))
