'''
Given a list of appointments, find all the conflicting appointments.
Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict.
'''

def get_all_appointments(intervals):
    i, j, start, end = 0, 1, 0, 1
    intervals.sort(key=lambda x:x[start])

    conflicts = []
    while j < len(intervals):
        if i == j:
            j += 1
        elif intervals[i][end] > intervals[j][start]:
            conflicts.append([intervals[i], intervals[j]])
            j += 1
        else:
            i += 1

    return conflicts


if __name__ == "__main__":
    for conflict in get_all_appointments([[4,5], [2,3], [3,6], [5,7], [7,8], [7,9]]):
        print("{} and {} conflict".format(conflict[0], conflict[1]))