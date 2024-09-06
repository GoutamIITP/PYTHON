for i in range(5):
    for j in range(5-i-1):
        print(" ",  end="")
    for j in range(2*i+1):
        print("*", end="")
    for j in range(5-i-1):
        print(" ",end="")
    print()

for i in range(5):
    # space
    for j in range(i):
        print(" ", end="")
    # staar
    for j in range(2*5-(2*i + 1)):
        print("*", end="")
    # sapce
    for j in range(i):
        print(" ", end=" ")
    print()

n = 5
for i in range(1,2*n):
    stars = i
    if (i > n):
        stars = 2*n-i
    for j in range(stars):
        print("*", end="")
    print()


