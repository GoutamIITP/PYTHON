'''Write a program to increment numeric strings by n'''

list = input("Enter list : \n").split()
n = int(input("Enter the number: \n"))
for x in list:
    if x.isnumeric():
        incre = int(x) + n
        print(" " +  str(incre), end=' ')
    else:
        print(" " + x, end=' ')
print()
