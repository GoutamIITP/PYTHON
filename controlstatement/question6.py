'''Write a program to calculate the sum of even fibonacci numbers below 4000'''

a , b = 0 , 1
c = 0
sum_even = 0
while c < 4000:
     
    a = b
    b = c
    c = a + b
    if (c % 2 == 0):
        sum_even += c
print("The sum of even fibonacci number is: ", sum_even)

