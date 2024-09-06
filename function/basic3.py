'''Create a recursive function
'''
def recurse(n):
    if n <= 1:
        return n
    return n + recurse(n -1)

res = recurse(10)
print(res)
