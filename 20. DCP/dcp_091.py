'''
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())

prints out 9 10 times
functions have closure and have access to the non-local variable i
'''

'''
In order to solve this issue, we should capture the value i when the funcionts are declared.
This would make i a local variable inside the anonymous functions.
'''


functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())
