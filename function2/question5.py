'''Write a function that return digital root of integer'''

def sod(X):
    if (X == 0):
        return 0
    else:
        return ((X % 10) + sod(X // 10))

n = int(input("Enter the number: "))
while (n >= 10):
    n = sod(n)

print("Didgital Root: ", n)