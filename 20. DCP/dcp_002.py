from heapq import heappush, heappop

start_factor_count = [2, 3, 5]


def populate_numbers(n, heap, regular_nums):
    if len(regular_nums) >= n:
        return

    low_num = heappop(heap)
    regular_nums.add(low_num)

    for k in start_factor_count:
        heappush(heap, low_num * k)
    
    populate_numbers(n, heap, regular_nums)
    

def get_n_regular(n):
    heap = []
    regular_nums = set()

    heappush(heap, 60)
    populate_numbers(n, heap, regular_nums)

    return sorted(regular_nums)


if __name__ == '__main__':
    regular_numbers = get_n_regular(10)
    print(regular_numbers)
