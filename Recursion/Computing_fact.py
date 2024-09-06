def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

# # iterative approach
# def factor(n):
#     fact = n
#     for i in range(1, n):
#         fact = fact * i
#     return fact

num = int(input("Enter the number"))
res = factorial(num)
print(res)
