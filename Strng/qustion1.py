n = input("Enter the sring: ")
l = [i for i in n.split()]

def printevenlength(itr,  list1):
    if itr == len(list1):
        return
    if len(list1[itr]) % 2 == 0:
        print(list1[itr])
    printevenlength(itr+1, list1)
    return

printevenlength(0, l)