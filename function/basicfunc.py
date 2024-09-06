'''Create a function with variable length of arguments'''


def Group(*args):
    for i in args:
        print(i)

 

Group(20, 40 ,80)
Group(80, 100)