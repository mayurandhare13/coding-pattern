'''
Happy Number (medium)
Any number will be called a happy number if, 
after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 
leads us to number ‘1’

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
2^2 + 3^2​ = 4 + 9 = 13
1^2 + 3^2 = 1 + 9 = 10
1^2 + 0^2 = 1 + 0 = 1

NOTE
Other number which are not happy number, also follows some pattern of repeating number
12 -> fast: 25, 85, (145, 20, 16, 58, repeatation -> 145, 20)...
'''

def find_happy_number(num):
    slow, fast = num, num

    while True:
        slow = find_digit_sq_sum(slow)
        fast = find_digit_sq_sum(find_digit_sq_sum(fast))
        print(f"slow: {slow}, fast: {fast}")
        if slow == fast:
            break           # found cycle | if slow become 1 then fast can also becomes 1
        
    return slow == 1


def find_digit_sq_sum(n):
    _sum = 0
    while n > 0:
        digit = n % 10
        _sum += digit * digit
        n = n // 10
    return _sum


if __name__ == "__main__":
    print(find_happy_number(23))
    print(find_happy_number(12))
