'''Write a program to find the sum of character ascii values in string list'''
s = input("Enter the string: \n").split()
sum = 0
 
for i in s:
    for a in i:
        sum += ord(a)
print(f"The sum is: {sum}")