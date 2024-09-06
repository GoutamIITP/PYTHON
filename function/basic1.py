'''Return multiples values form a function'''

def calculation(a, b):
    return a + b, a - b

add, sum = calculation(40, 10)
print(add, sum)