'''Write a program to find gcd of two number'''

def gcd(a, b):
    if a == 0:
        return a
    if b == 0:
        return b

    if a == b:
        return a

    if a > b:
        if a % b == 0:
            return b
        return gcd(a-b, b)
    if b % a == 0:
        return a
    return gcd(a,b-a)

a = 98
b = 56
print(f"GCD of {a} and {b} is {gcd(a,b)}")