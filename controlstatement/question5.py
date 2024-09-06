'''print the prime number between 1 to  100'''
n = int(input("Enter the number"))
for i in range(1, n + 1):
    f = 0
    for j in range(2, (i // 2) + 1):
        if (i % j == 0): 
            f = 1     
            break
    if (f == 0):
            print(i, end=" ")


n = int(input("Enter the number: "))

 
if n <= 1:
    print(f"{n} is not a prime number")
else:
    f = 0
    for j in range(2, (n // 2) + 1):
        if n % j == 0:
            f = 1
            break

    if f == 0:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")