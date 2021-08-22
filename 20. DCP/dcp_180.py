from queue import Queue


def interleave(stack: list, que: Queue, index = 1):
    for _ in range(len(stack) - index):
        que.put(stack.pop())
    
    while not que.empty():
        stack.append(que.get())

    if len(stack) - index > 1:
        interleave(stack, que, index + 1)


if __name__ == '__main__':
    stack = [1, 2, 3, 4, 5]
    que = Queue()
    interleave(stack, que)
    assert stack == [1, 5, 2, 4, 3]

    stack = [1, 2, 3, 4]
    que = Queue()
    interleave(stack, que)
    assert stack == [1, 4, 2, 3]
