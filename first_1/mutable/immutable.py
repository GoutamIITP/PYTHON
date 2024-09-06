#immutable
def myfunc1(a):
    print("\t Inside myfunc1()")
    print("\t Value recevied in 'a' as", a)
    a = a + 2
    print("\t Value of 'a'  now changes to", a)
    print("\t returning from myfunc1()")

#__main__
num = 3
print("Calling myfunc1() by passing 'num' with value", num)
myfunc1(num)
print("Back from myfunc(). Value of'num' is", num)

#mutable
def myfunc2(myList):
    print("\n\t Inside called function now")
    print("\t List recieved:", myList)
    myList[0] += 2
    print("\t List within called function, after changes:",myList)
    return

List1 = [1]
print("\n List before function call:",List1)
myfunc2(List1)
print("\n List after function call:", List1)