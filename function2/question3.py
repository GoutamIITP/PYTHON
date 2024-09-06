'''Write user defined function to check that the input pair be of number is amicable '''
def isamicable(a, b):
    i = 1
    j = 1
    asum = 0
    bsum = 0
    while (i < a):
        if (a % i ==0):
            asum  += i
        i= i+1
    while (j < b):
        if (b % j ==0):
            bsum +=j
        j = j + 1
    if (asum == b and bsum  == a):
        print(f"{a} and {b} are amicable")
    else:
        print(f"{a} and {b} are not amicable")



a = int(input("Enter the number"))
b = int(input("Enter the number"))
 
# sum1 = 0
# for i in range(1, int(a/2) + 1):
#     if (a % i == 0):
#         sum +=i
# for j in range(1, int(b/2) + 1):
#     if (a % j ==0:)

isamicable(a, b)