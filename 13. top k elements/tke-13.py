'''
Scheduling Tasks (hard) 

You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can't be run again. If the cooling period for all tasks is 'K' intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can't execute any task then it must stay idle.

Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a
'''


from heapq import *


def schedule_tasks(tasks, k):
    intervalCount = 0
    tasksFrequencyMap = {}
    for task in tasks:
        tasksFrequencyMap[task] = tasksFrequencyMap.get(task, 0) + 1
    
    # add all tasks to the max heap
    maxHeap = []
    for char, freq in tasksFrequencyMap.items():
        heappush(maxHeap, (-freq, char))

    while maxHeap:
        waitList = []
        n = k + 1   # try to execute as many as k+1 tasks (including itself) from max heap
        
        while maxHeap and n > 0:
            intervalCount += 1
            n -= 1
            freq, char = heappop(maxHeap)
            if -freq > 1:
                # decrement the frequency
                waitList.append((freq + 1, char))
        
        # putting all waitlist back to the max heap
        for freq, char in waitList:
            heappush(maxHeap, (freq, char))

        # add idle time
        if maxHeap:
            intervalCount += n

    return intervalCount


if __name__ == "__main__":
    print(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2))
    print(schedule_tasks(['a', 'b', 'a'], 3))
