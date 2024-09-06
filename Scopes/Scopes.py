x = 99
# def func(y):
#     z = x + y
#     return z

# res = func(1)
# print(res)    

# def func1():
#     global x
#     x = 70

# func1()
# print(x)

# def f1():
#     x = 88
#     def  f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))